# coding:utf-8
import requests
import json
# 失败，豆瓣做了反爬虫处理，根据浏览器访问获取的json url链接和再次打开后的url根本返回不一样。还不知道怎么解决

class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&callback=jsonp1&start={}&count=18&loc_id=108288&_=1551928951397"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        print(json_str)
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        return content_list

    def save_content_list(self, content_list):
        with open("douban.txt", "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")

    def run(self):
        num = 0
        url = self.url_temp.format(num)
        json_str = self.parse_url(url)
        content_list = self.get_content_list(json_str)
        self.save_content_list(content_list)
        while len(content_list) < 18:
            break
        num += 18


if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()
