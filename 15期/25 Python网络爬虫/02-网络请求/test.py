# coding:utf-8
from urllib import request

resp = request.urlopen("http://www.baidu.com")
print(resp.read())
