# -*- coding: utf-8 -*-
import scrapy


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['http://d.wz.sun0769.com']
    start_urls = ['http://d.wz.sun0769.com/index.php/question/huiyin?page=0']

    def parse(self, response):
        pass
