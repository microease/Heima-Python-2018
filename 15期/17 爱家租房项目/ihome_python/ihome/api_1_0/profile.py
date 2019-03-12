# coding:utf-8
from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET
from ihome.utils.image_storagr import storage
from ihome.models import User
from ihome import db


@api.route("/users/avatar", method=["POST"])
@login_required
def set_user_avatar():
    # 设置用户的头像
    # 装饰器的代码中已经将user_id保存到了g对象中，所以视图中可以直接读取
    user_id = g.user_id
    image_file = request.files.get("avator")
    if image_file is None:
        return jsonify(errno=RET.PARAMERT, errmsg="未上传图片")
    image_data = image_file.read()
    try:
        file_name = storage(image_data)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传图片失败")
    # 保存文件名到数据库中
    try:
        User.query.filter_by(id=user_id).update({"avatar_url": file_name})
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="保存图片信息失败")
    # 保存成功返回
    return jsonify(errno=RET.OK, errmsg="保存成功",data={"avatar_url":})
