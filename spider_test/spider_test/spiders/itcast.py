# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import sys
import codecs
sys.path.append('../')
from common import utils
from urllib.parse import urlparse

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    url_root = "http://www.itcast.cn/"
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        print(response.url)
        file_relative = self.get_file_relative(response)
        utils.mkdirs_by_relative(file_relative)
        with codecs.open(file_relative, 'wb') as f:
            f.write(response.body)

        # 遍历网页图片
        all_image_urls = self.getAllImageUrls(response)
        for image_url in all_image_urls:
            yield response.follow(image_url, callback=self.parseImage)

    def parseImage(self, response):
        #图片只需保存就好了
        file_relative = self.get_file_relative(response)
        utils.mkdirs_by_relative(file_relative)
        with codecs.open(file_relative, 'wb') as f:
            f.write(response.body)

    def getAllImageUrls(self,response):
        link_list = response.xpath('//*/img')
        ret = []
        for k,link in enumerate(link_list):
            img_url = link.xpath('@src').get() or link.xpath('@data-original').get()
            if img_url:
                ret.append(img_url)

        return ret
    def get_file_relative(self,response):
        file_relative = ""
        if response.url:
            file_relative = urlparse(response.url).path
        return "../../out" + file_relative

def start_spider():
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'items.json'
    })
    process.crawl(ItcastSpider)
    process.start()  # the script will block here until the crawling is finished

start_spider()