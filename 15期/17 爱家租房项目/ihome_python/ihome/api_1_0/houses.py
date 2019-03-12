# coding:utf-8
from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET
from ihome.utils.image_storage import storage
from ihome.models import User, Area
from ihome import db, constants

area_li = None


@api.route("/areas", method=["GET"])
def get_area_info():
    # 获取城区信息
    try:
        area_li = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据库错误")
    area_dict_li = []
    for area in area_li:
        area_dict_li.append(area.to_dict())
    return jsonify(errno=RET.OK, errmsg="OK", data=area_dict_li)
