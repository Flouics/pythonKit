# -*- coding: utf-8 -*-
import scrapy
import sys
import codecs
sys.path.append('../')
from common import utils
from urllib.parse import urlparse
from spiderClone.items import SpiderCloneItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        print(response.url)
        file_relative = self.get_file_relative(response)
        utils.mkdirs_by_relative(file_relative)
        with codecs.open(file_relative, 'wb') as f:
            f.write(response.body)

        # 遍历网页图片
        yield self.getAllImage(response)
        #self.getAllResFiles(response)

    def parseDownFile(self, response):
        #只需下载就好了
        file_relative = self.get_file_relative(response)
        utils.mkdirs_by_relative(file_relative)
        with codecs.open(file_relative, 'wb') as f:
            f.write(response.body)

    # 遍历网页图片
    def getAllImage(self,response):
        print("=======>>>>>>")
        link_list = response.xpath('//*/img')
        all_image_urls = []
        for k,link in enumerate(link_list):
            img_url = link.xpath('@src').get() or link.xpath('@data-original').get()
            if img_url:
                all_image_urls.append(img_url)
        for image_url in all_image_urls:
            print(image_url)
            yield response.follow(image_url, callback=self.parseDownFile)

    # 遍历文件 css
    def getAllResFiles(self,response):
        #<link rel="stylesheet" href="/2018czgw/css/reset.css">
        link_list = response.xpath('//link[@rel="stylesheet"]')
        print("============",link_list.getall())
        all_urls = []
        for k,link in enumerate(link_list):
            url = link.xpath('@href').get()
            if url:
                all_urls.append(url)
        for url in all_urls:
            print(url)
            yield response.follow(url, callback=self.parseDownFile)

    def get_file_relative(self,response):
        file_relative = ""
        if response.url:
            file_relative = urlparse(response.url).path
        if file_relative == "/":
            file_relative = "/index.html"
        return "out" + file_relative

