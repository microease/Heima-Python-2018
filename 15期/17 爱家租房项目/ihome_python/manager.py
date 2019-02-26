# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)


class Config(object):
    """配置信息"""
    DEBUG = True
    SECRET_KEY = "SFJSAKLFHASLKJHASKNDMSBN"
    # 数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome_python"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"


app.config.from_object(Config)
db = SQLAlchemy(app)

# 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    app.run()
