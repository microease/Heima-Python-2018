# coding:utf-8
from flask import Flask, request, abort
import hashlib

# 常量
WECHAT_TOKEN = "huyankai"

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


if __name__ == '__main__':
    app.run(port=8000, debug=True)
