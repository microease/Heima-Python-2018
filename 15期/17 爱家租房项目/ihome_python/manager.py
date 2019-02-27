# coding:utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_session import Session
from flask_wtf import CSRFProtect
from config import config_map


# 工厂模式
def create_app(config_name):
    """
    创建Flask的应用对象
    :param config_name:string 配置模式的名字
    :return:
    """
    app = Flask(__name__)
    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)
    return app


app = create_app("develop")
db = SQLAlchemy(app)

# 创建redis连接对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 利用flask_session，将session数据保存到redis中
Session(app)
# 为Flask补充csrf防护
CSRFProtect(app)


@app.route("/index")
def index():
    return "index page"


if __name__ == '__main__':
    app.run()
