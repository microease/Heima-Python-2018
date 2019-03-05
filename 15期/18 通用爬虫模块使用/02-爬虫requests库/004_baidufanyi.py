import requests

data = {
    "from": "en",
    "to": "zh",
    "query": "hello",
    "transtype": "translang",
    "simple_means_flag": "3",
    # "sign": "58244.262325",
    "token": "d93fbaa6c6a12f54a4cd1671b7d04dfb",
}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
url = "https://fanyi.baidu.com/v2transapi"
response = requests.post(url, data=data, headers=headers)
print(response.content.decode())
