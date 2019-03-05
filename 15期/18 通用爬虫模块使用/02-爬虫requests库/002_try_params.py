# coding:utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

p = {"wd": "传智播客"}
url_temp = "https://www.baidu.com/s?"

response = requests.get(url_temp, headers = headers,params=p)
print(response.content.decode())
print(response.request.url)
