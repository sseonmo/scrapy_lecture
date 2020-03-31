# -*- coding: utf-8 -*-
import scrapy
from ..items import ItArticle as article

# Scrapy Feed Export 실습

# 출력형식
# JSON, JSON Lines
# CSV
# XML, Pickle, Marshal

# 저장위치
# Local File System
# FTP - server
# S3 - aws
#  console

# 방법 2가지
# 1. 커멘트 이용 : ( --output, -o), (--output-format, -t)
# 옵션 설정 예) --set=FEED_EXPORT_INDENT=2
# 2. Settings.py 이용
# 자동으로 저장(파이면, 형식, 위치 지정가능)


class TestSpider(scrapy.Spider):
    name = 'test7'
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