import requests

response = requests.get("http://www.baidu.com")
status_code = response.status_code
header = response.headers
user_agent = response.request.headers
print(status_code)
print(header)
print(user_agent)
print(response.content.decode())
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
response = requests.get("http://www.baidu.com",headers = headers)
print(response.content.decode())
user_agent = response.request.headers

print(user_agent)
