# coding=utf8
import requests
import re
import json
url = "https://36kr.com/"
response = requests.get(url).content.decode()
# print(response)
ret = re.findall("<script>var props=(.*?)</script>",response)[0]
with open("36kr.json","w",encoding="utf-8") as f:
    f.write(ret)
ret = json.loads(ret)
print(ret)