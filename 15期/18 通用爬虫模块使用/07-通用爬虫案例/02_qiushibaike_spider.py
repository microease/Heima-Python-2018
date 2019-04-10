# coding:utf-8
import requests
from lxml import etree


class QiushibaikeSpider:
    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        }

    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1, 14)]

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):
        html = etree.HTML(html_str)
        li_list = html.xpath(".//div[@class='recommend-article']/ul/li")
        for li in li_list:
            item = {}
            item["content"] = li.xpath(".//div[@class='recmd-right']/a/text()")
            item["href"] = li.xpath(".//div[@class='recmd-right']/a/@href")
            item["like"] = li.xpath(".//div[@class='recmd-right']/div[@class='recmd-detail']/div[@class='recmd-num']/span[0]")

    def run(self):
        # 1 url_list
        url_list = self.get_url_list()
        # 2 遍历发送请求 获取响应
        for url in url_list:
            html_str = self.parse_url(url)
        # 3 提取数据
        # 4 保存
        pass
