# coding:utf-8
# Author :      microease
# Date :       2019/4/30

from urllib import request, parse

url = "http://www.baidu.com/s?wd=python"
result = parse.urlparse(url)
result2 = parse.urlsplit(url)

print(result)
print(result2)
