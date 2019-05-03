# -*- coding: utf-8 -*-
import scrapy


class MicroeaseSpider(scrapy.Spider):
    name = 'microease'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
