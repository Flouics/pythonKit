# -*- coding: utf-8 -*-
import scrapy


class Sp1Spider(scrapy.Spider):
    name = 'sp_1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        pass
