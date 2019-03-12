# coding:utf-8
from . import api
from ihome.utils.commons import login_required
from flask import g, current_app, jsonify, request
from ihome.utils.response_code import RET
from ihome.utils.image_storagr import storage

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
