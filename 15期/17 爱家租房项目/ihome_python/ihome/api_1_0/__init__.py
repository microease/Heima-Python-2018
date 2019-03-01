# coding:utf-8

from flask import Blueprint


# 创建蓝图对象
api = Blueprint("api_1_0", __name__)


# 导入蓝图的视图
from . import demo, verify_code, passport
