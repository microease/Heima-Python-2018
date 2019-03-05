# coding:utf-8
import requests

session = requests.session()
renren_login = "http://www.renren.com/PLogin.do"
post_data = {"email": "173418535@qq.com", "password": "huyankai"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
session.post(renren_login, data=post_data, headers=headers)
r = session.get("http://www.renren.com/863482774/profile", headers=headers)
print(r.status_code)
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
