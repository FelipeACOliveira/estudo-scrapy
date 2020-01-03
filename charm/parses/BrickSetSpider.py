import scrapy
import pandas as pd

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        css_selector = '.set'

        for brickset in response.css(css_selector):
            name_selector = 'h1 a ::text'

            document = {
                'id': brickset.css(name_selector).getall()[0].strip()[:-1],
                'name': brickset.css(name_selector).getall()[1].strip()
            }

            print(document)
