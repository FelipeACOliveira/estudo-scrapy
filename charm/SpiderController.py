from BrickSetSpider import BrickSetSpider
import scrapy
from scrapy.crawler import CrawlerProcess

settings={
    'FEED_FORMAT': 'json'
}

process = CrawlerProcess(settings)

process.crawl(BrickSetSpider)
process.start()


