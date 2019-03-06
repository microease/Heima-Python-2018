# coding:utf-8
import requests
import json
import sys


class BaiduFanyi:
    def __init__(self, trans_str):
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.trans_str = trans_str
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        }

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.loads(response.content.decode())

    def get_ret(self, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print(ret)

    def run(self):
        # 实现主要逻辑
        lang_detect_data = {"query": self.trans_str}
        # 1 获取语言类型
        # 2 准备post数据
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]

        # 3 发送请求获取响应
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else \
            {"query": self.trans_str, "from": "en", "to": "zh"}
        # 4： 提取翻译结果
        dict_response = self.parse_url(self.trans_url, trans_data)
        print(dict_response)
        self.get_ret(dict_response)


if __name__ == '__main__':
    trans_str = sys.argv[1]
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()
