from scrapy.crawler import CrawlerProcess
from spiderClone.spiders.itcast import ItcastSpider
from scrapy.utils.project import get_project_settings

def start_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(ItcastSpider)
    process.start()  # the script will block here until the crawling is finished

start_spider()