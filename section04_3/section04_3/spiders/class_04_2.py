# -*- coding: utf-8 -*-
import scrapy
from ..items import SiteRankItems

class TestSpider(scrapy.Spider):
    name = 'test10'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://www.alexa.com/topsites/']

    def parse(self, response):
        """
        :param response:
        :return:  SiteRankItems
        """
        for p in response.css('div.site-listing'):
            # 아이템 객체 생성
            item = SiteRankItems()
            item['rank_num'] = p.xpath('div[@class="td"]/text()').get()
            item['site_name'] = p.xpath('div[@class="td DescriptionCell"]/p/a/text()').get()
            right = p.xpath('div[@class="td right"]/p/text()').getall()
            item['daily_time_site'] = right[0]
            item['daily_page_view'] = right[1]
            yield item
            # print(p.xpath('//div[@class="DescriptionCell"]/p/a/text()').get())

