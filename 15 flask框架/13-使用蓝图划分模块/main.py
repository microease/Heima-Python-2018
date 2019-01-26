# coding=utf-8
from flask import Flask
from orders import app_orders
from cart import app_cart

app = Flask(__name__)
# app.route("/get_goods")(get_goods)
# app.route("/register")
app.register_blueprint(app_orders)
app.register_blueprint(app_orders, url_prefix="/orders")
app.register_blueprint(app_cart, url_prefix="/cart")


@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    print(app.url_map)
    app.run()
