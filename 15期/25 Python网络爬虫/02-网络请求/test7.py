# coding:utf-8
# File Name：     test7
# Description :
# Author :       huxiaoyi
# Date：          2019-05-03
from urllib import request

url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())
# b'{\n  "origin": "119.123.42.99, 119.123.42.99"\n}\n'
handler = request.ProxyHandler({"http": "112.85.129.250:9999"})

opener = request.build_opener(handler)

resp = opener.open(url)

print(resp.read())
# b'{\n  "origin": "112.85.129.250, 112.85.129.250"\n}\n'
