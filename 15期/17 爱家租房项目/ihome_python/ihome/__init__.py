# coding:utf-8
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from flask_wtf import csrf
import logging
import redis
from logging.handlers import RotatingFileHandler
db = SQLAlchemy()

# 创建redis连接对象
redis_store = None
csrf = CSRFProtect()

logging.error("ssd")  # 错误信息记录
logging.warn("ssd")  # 警告信息记录
logging.info("ssd")  # 消息提示信息记录
logging.debug("ssd")  # 调试信息记录

# 设置日志等级
logging.basicConfig(level=logging.DEBUG)
# 创建日志记录器
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志记录的格式
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
logging.getLogger().addHandler(file_log_handler)


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
    # 使用app初始化db
    db.init_app(app)
    # 初始化redis工具
    global redis_store
    redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    # 利用flask_session，将session数据保存到redis中
    Session(app)
    # 为Flask补充csrf防护
    CSRFProtect(app)
    # 注册蓝图
    from ihome import api_1_0
    app.register_blueprint(api_1_0.api, url_prefix="/api/v1.0")
    return app
