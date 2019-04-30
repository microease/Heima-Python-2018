# coding:utf-8
# Author :      microease
# Date :       2019/4/29

from urllib import request
from urllib import parse

url = 'http://www.baidu.com/s'

params = {'wd': '张三',
          }
result = parse.urlencode(params)

print(result)

url = url + "?" + result

print(url)

