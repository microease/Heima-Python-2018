# coding=utf-8
from flask import Flask, Blueprint

# 创建蓝图对象,蓝图就是一个小模块的概念

app_orders = Blueprint("app_orders", __name__, template_folder="templates")


@app_orders.route("/get_orders")
def get_orders():
    return "get orders page"


@app_orders.route("post_orders")
def post_orders():
    pass
