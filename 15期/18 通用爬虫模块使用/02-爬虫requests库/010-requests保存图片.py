# coding:utf-8
import requests
import re

url = "http://cn.python-requests.org/zh_CN/latest/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
}
response = requests.get(url, headers=headers)
res = response.content.decode("utf-8")
pattern = re.compile(r'<img .*? src="(.*?).png"', re.S)
match = re.findall(pattern, res)
print(match)
j = 0
for i in match:
    f = open(str(j)+".png","wb")
    res = requests.get(i).content
    print(res)
    f.write(res)
    f.close()
    j+=1
