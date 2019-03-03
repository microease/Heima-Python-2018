# coding:utf-8
import redis
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
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期 秒


class DevelopmentConfig(Config):
    # 开发模式
    DEBUG = True


class ProductConfig(Config):
    # 生产环境
    pass


config_map = {
    "develop": DevelopmentConfig,
    "product": ProductConfig
}
