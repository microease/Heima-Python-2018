# coding:utf-8
# Author :     microease
# Date :       2019/4/22
from selenium import webdriver


class DouyuSpider:
    def __init__(self):
        self.start_url = "https://www.douyu.com/g_LOL/all"
        self.driver = webdriver.Chrome()

    def get_content_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["room_img"] = li.find_element_by_xpath("../span[@class='imgbox']/img").get_attribute("src")
            item["room_title"] = li.find_element_by_xpath("./a").get_attribute("title")
            item["room_cate"] = li.find_element_by_xpath(".//span[@class='tag ellipsis']").text
            item["anchor_name"] = li.find_element_by_xpath(".//span[@class='dy-name ellipsis fl']").text
            item["watch_num"] = li.find_element_by_xpath(".//span[@class='dy-num fr']").text
            content_list.append(item)
        next_url = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        return content_list, next_url

    def save_content_list(self, content_list):
        pass

    def run(self):
        # start_url
        # 发送请求 获取响应
        self.driver.get(self.start_url)
        # 提取数据，提取下一页的按钮
        content_list, next_url = self.get_content_list()
        # 保存数据
        self.save_content_list(content_list)
        # 点击下一页元素
        next_url.click()


if __name__ == '__main__':
    douyu = DouyuSpider()
    douyu.run()
