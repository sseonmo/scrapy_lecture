# -*- coding: utf-8 -*-
import scrapy
from ..items import ItArticle as article

class TestSpider(scrapy.Spider):
    name = 'test6'
    allowed_domains = ['itnews.com']
    start_urls = ['https://www.itnews.com/']

    def parse(self, response):
        """
        :param response:
        :return: request
        """
        for url in response.css('div.hed > div.title > a::attr(href)').getall():
            # self.logger.info(response.urljoin(url))
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """
        :param response:
        :return: item
        """

        item = article()
        item['title'] = response.xpath('//header[@class="cat"]/h1/text()').extract_first()
        # item['img_url'] = response.xpath('//figure/img/@src').get()
        item['img_url'] = response.xpath('//img[@itemprop="contentUrl"]/@data-original').get()
        item['contents'] = ''.join(response.xpath('//div[@id="drr-container"]/p/text()').extract())

        self.logger.info(dict(item))

        yield item