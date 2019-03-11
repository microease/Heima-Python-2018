# coding:utf-8
# 图片验证码的redis有效期
IMAGE_CODE_REDIS_EXPIERS = 180
# 短信验证码的redis有效期，单位秒
SMS_CODE_REDIS_EXPIRES = 300
# 发送短信验证码的间隔，秒
SEND_SMS_CODE_INTERVAL = 60
# 登录错误尝试次数
LOGIN_ERROR_MAX_TIMES = 3
# 登录错误限制的时间
LOGIN_ERROR_FORBID_TIME = 600