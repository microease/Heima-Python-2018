# coding:utf-8
import requests

proxies = {"http": "http://175.165.210.8:35316"}
user_agent = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

re = requests.get("http://www.baidu.com", proxies=proxies, headers=user_agent)
print(re.status_code)
