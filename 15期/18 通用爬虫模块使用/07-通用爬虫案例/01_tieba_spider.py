# coding:utf-8
import requests
from lxml import etree
import json


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "" + tieba_name
        self.headers = ""

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_image_list(self, detail_url,total_img_list):
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)

    def save_content_list(self, content_list):
        file_path = self.tieba_name + ".txt"
        with open(file_path, "a") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False, indent=2))
                f.write("\n")

    def run(self):
        next_url = self.start_url
        while next_url is not None:
            # 发送请求 获取响应
            html_str = self.parse_url(self.start_url)
            # 提取数据
            content_list, next_url = self.get_content_list(html_str)
            # 保存数据
            self.save_content_list(content_list)
