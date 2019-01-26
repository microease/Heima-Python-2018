# coding=utf-8
from flask import render_template
from . import app_cart


def get_cart():
    return render_template("cart.html")
