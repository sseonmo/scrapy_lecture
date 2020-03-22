# -*- coding: utf-8 -*-
import scrapy


class Class021Spider(scrapy.Spider):
    name = 'test2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
        :param response:
        :return: Title Text
        """
        # 2가지 (CSS Selector, XPath)
        # get() [하나만 가져오기] <-> getall() [전체] / extract_first() <-> extract()

        # 예제 1( css Selector)
        # css
        # -o 파일명.확장자, -t 파일타입(json, jsonlines, jl, csv, xml, marshal, pickle)
        for text in response.css('div.post-header h2 a::text').getall():
            # return Type : Requset, BaseItem, Dictionary, NOne
            yield {
                'title': text
            }

        # 예제 2( Xpath )
        # for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
        #     yield {
        #         'number': i,
        #         'title': text
        #     }