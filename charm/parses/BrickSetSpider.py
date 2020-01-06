import scrapy
import pandas as pd


class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        xpath_selector = '//div/h1/a'

        for brickset in response.xpath(xpath_selector):
            id_selector = 'span/text()'
            name_selector = 'text()'

            document = {
                'id': brickset.xpath(id_selector).get().strip()[:-1],
                'name': brickset.xpath(name_selector).get().strip()
            }



