# coding=utf-8
from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def index():
    # 接受参数
    user_name = request.form.get("user_name")
    password = request.form.get("password")

    # 参数判断
    if not all([user_name, password]):
        resp = {
            "code": 1,
            "message": "invalid params"
        }
        return jsonify(resp)
    if user_name == "admin" and password == "python":
        resp = {
            "code": 0,
            "message": "login success"
        }
        return jsonify(resp)
    else:
        resp = {
            "code": 2,
            "message": "wrong user name or password"
        }
        return jsonify(resp)
    return "index page"


if __name__ == '__main__':
    app.run(debug=True)
