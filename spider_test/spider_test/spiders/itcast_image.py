# -*- coding: utf-8 -*-
import scrapy
import sys
import codecs
sys.path.append('../')
from common import utils
from urllib.parse import urlparse

class ItcastImageSpider(scrapy.Spider):
    name = 'itcast_image'
    allowed_domains = ['itcast.cn']
    url_root = "http://www.itcast.cn/"
    start_urls = ['http://www.itcast.cn/images/teacher/20151525101531117.jpg']

    def parse(self, response):
        print(response.url)
        file_relative = self.get_file_relative(response)
        utils.mkdirs_by_relative(file_relative)
        with codecs.open(file_relative, 'wb') as f:
            f.write(response.body)

    def get_file_relative(self,response):
        file_relative = ""
        if response.url:
            file_relative = urlparse(response.url).path
        return "out" + file_relative
