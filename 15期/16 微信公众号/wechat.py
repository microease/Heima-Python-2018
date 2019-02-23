# coding:utf-8
from flask import Flask, request, abort, render_template
import hashlib
import urllib2

# 常量
WECHAT_TOKEN = "huyankai"
WECHAT_APPID = "A"
WECHAT_SECRECT = "B"
app = Flask(__name__)


@app.route("/wechat8000")
def wechat():
    # 接收微信参数
    signature = request.args.get('signature')
    timestamp = request.args.get('timestamp')
    nonce = request.args.get('nonce')
    echostr = request.args.get('echostr')
    # 数据校验
    if not all([signature, timestamp, nonce, echostr]):
        abort(400)
    # 按照微信的流程进行计算签名
    # 进行字典序排序
    li = [WECHAT_TOKEN, timestamp, nonce]
    # 排序
    li.sort()
    # 拼接字符串
    tmp_str = "".join(li)
    # 进行sha1加密，得到正确的签名值
    sign = hashlib.sha1(tmp_str).hexdigest()
    # 将自己得出的参数和请求的签名参数进行对比，如果相同，则证明请求的参数来自微信的服务器，是正确的参数
    if signature != sign:
        # 表示请求不是来自微信
        abort(403)
    else:
        return echostr


@app.route("/wechat8000/index")
def index():
    # 让用户通过微信访问的网页视图
    # 从微信服务器中拿去用户的资料数据
    code = request.args.get("code")
    if not code:
        return u"缺失code参数"
    url = ""
    response = urllib2.urlopen(url)
    # 获取响应体数据，微信返回的json数据
    json_str = response.read()
    resp_dict = json.loads(json_str)

    # 提取access_token
    if "errcode" in resp_dict:
        return u"获取access_token失败"
    access_token = resp_dict.get("access_token")
    open_id = resp_dict.get("openid")
    url = ""
    response = urllib2.urlopen(url)
    user_json_str = response.read()
    user_dict_data = json.loads(user_json_str)

    if "errcode" in user_dict_data:
        return u"获取用户信息失败"
    else:
        # 将用户的数据填充到页面中
        return render_template("index.html",user = user_dict_data)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
