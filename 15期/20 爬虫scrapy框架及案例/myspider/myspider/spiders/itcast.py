# -*- coding: utf-8 -*-
import scrapy


class MicroeaseSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1) 16分钟
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            item['name'] = li.xpath(".//h3/text()").extract()[0]
            item['title'] = li.xpath(".//h4/text()").extract()[0]
        print(item)
