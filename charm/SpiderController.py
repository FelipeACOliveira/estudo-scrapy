from BrickSetSpider import BrickSetSpider
from scrapy.crawler import CrawlerProcess


class SpiderController(object):
    def __init__(self):
        settings = {
            'FEED_FORMAT': 'json'
        }

        process = CrawlerProcess(settings)

        process.crawl(BrickSetSpider)
        process.start()