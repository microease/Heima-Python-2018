# coding:utf-8
# Author :      microease
# Date :       2019/4/30
from urllib import request

url = "https://www.lagou.com/zhaopin/Python/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
}

resp = request.urlopen(url)
print(resp.read())