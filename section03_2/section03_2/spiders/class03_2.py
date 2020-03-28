# -*- coding: utf-8 -*-
import scrapy

# import 해서 logger 사용하는 방법
# import logging
# logger = logging.getLogger('Mylogger')

# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']
    # 실행방법 1
    # 멀티도메인
    start_urls = ['https://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    # 사용자 시스템 설정 ( settings.py )
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'COOKIES_ENABLED': True,
    }
    # 실행방법2
    # Request 각각지정
    # def start_requests(self):
    #     yield scrapy.Request('http://blog.srapinghub.com/', self.parse1())
    #     yield scrapy.Request('htts://naver.com', self.parse2())
    #     yield scrapy.Request('https://daum.net', self.parse3())

    def parse1(self, response):
        pass

    def parse2(self, response):
        pass

    def parse3(self, response):
        pass

    def parse(self, response):
        # logger 사용
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response status : %s' % response.status)

        if response.url.find('scrapinghub'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
