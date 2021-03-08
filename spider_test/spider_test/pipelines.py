# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderTestImagesPipeline(object):
    def process_item(self, item, spider):
        print("==================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print(item)
        return item

class SpiderTestFilesPipeline(object):
    def process_item(self, item, spider):
        print("++++++++++++++++++++++++>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        return item
