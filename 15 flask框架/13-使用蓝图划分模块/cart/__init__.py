# coding=utf-8

from flask import Blueprint

app_cart = Blueprint("app_cart", __name__)

from .views import get_cart
