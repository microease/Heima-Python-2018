# coding:utf8
# Author :       huxiaoyi
# Date：         2019-05-02
# Time：         20:14
from urllib import request

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'

}
url = "https://www.lagou.com/zhaopin/Python/"

req = request.Request(url, headers=headers)
resp = request.urlopen(req)
print(resp.read().decode())
