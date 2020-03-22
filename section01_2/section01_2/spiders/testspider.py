# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        print('dir', dir(response))
        print('status', response.status)
        print('text', response.body)
