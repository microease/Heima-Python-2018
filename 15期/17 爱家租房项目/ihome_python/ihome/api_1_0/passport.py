# coding:utf-8

from . import api
from flask import request, jsonify, current_app, session
from ihome.utils.response_code import RET
from ihome import redis_store, db, constants
from ihome.models import User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
import re


@api.route("/users", method=["POST"])
def register():
    req_dict = request.get_json()
    mobile = req_dict.get("mobile")
    sms_code = req_dict.get("sms_code")
    password = req_dict.get("password")
    password2 = req_dict.get("password2")

    if not all([mobile, sms_code, password, password2]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
    # 判断手机号格式
    if not re.match(r"1[34578]\d{9}", mobile):
        # 格式不对
        return jsonify(errno=RET.PARAMERR, errmsg="手机号格式错误")
    if password != password2:
        return jsonify(errno=RET.PARAMERR, errmsg="两次密码不一致")
    # 从redis中提取短信验证码
    try:
        real_sms_code = redis_store.get("sms_code_%s" % mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="读取真实验证码异常")
    # 判断短信验证码是否过期
    if real_sms_code is None:
        return jsonify(errno=RET.NODATA, errmsg="短信验证码失效")
    # 判断用户填写短信验证码的正确性
    if real_sms_code != sms_code:
        return jsonify(errno=RET.DATAERR, errmsg="短信验证码错误")
    # 判断用户的手机号是否注册过
    # try:
    #     user = User.query.filter_by(mobile=mobile).first()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    # else:
    #     if user is not None:
    #         # 表示手机号已存在
    #         return jsonify(errno=RET.DATAEXIST, errmsg="手机号已经存在！")

    # 保存用户的注册数据到数据库中
    user = User(name=mobile, password_hash=password, mobile)
    try:
        db.session.add(user)
        db.session.commit()
    except IndentationError as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAEXIST, errmsg="手机号已经存在")
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库异常")
    # 保存登录状态到session中
    # 返回登录后的结果
    session["name"] = mobile
    session["mobile"] = mobile
    session["user_id"] = user.id
    return jsonify(errno=RET.OK, errmsg="注册成功")


@api.route("sessions/", method=["POST"])
def login():
    pass
    # 获取参数，校验参数：参数完整校验，手机号格式校验，判断错误次数是否超过限制，如果超过限制，则返回
    # 从数据库中根据手机号查询用户的数据对象，用数据库的密码与用户填写的密码进行对比验证，如果验证成功，保存登录状态，如果验证失败，返回提示信息，并记录错误次数。
    req_dict = request.get_json()
    mobile = req_dict.get("mobile")
    password = req_dict.get("password")
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数不完整")
    if not re.match(r"1[34578]\d{9}", mobile):
        return jsonify(errno=RET.PARAMERR, errmsg="手机号格式错误")
    user_ip = request.remote_addr  # 获取用户ip
    try:
        access_nums = redis_store.get("access_nums_%s" % user_ip)
    except Exception as e:
        current_app.logger.error(e)
    else:
        if access_nums is not None and int(access_nums) > constants.LOGIN_ERROR_MAX_TIMES:
            return jsonify(errno=RET.REQERR, errmsg="尝试错误次数过多，请稍后重试")
    try:
        user = User.query.filter_by(mobile=mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="获取用户信息失败")
    if user is None or not user.check_password(password):
        try:
            redis_store.incr("access_num_%s" % user_ip)
            redis_store.expire("access_num_%s" % user_ip, constants.LOGIN_ERROR_FORBID_TIME)
        except Exception as e:
            current_app.logger.error(e)

        return jsonify(errno=RET.DATAERR, errmsg="用户名或密码错误")
    session["name"] = user.name
    session["mobile"] = user.mobile
    session["user_id"] = user.id
    return jsonify(errno=RET.OK,errmsg="登录成功")