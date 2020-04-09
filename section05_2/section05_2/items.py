# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItems(scrapy.Item):
    # 기사제목, 기시본문, 요청리스트 페이지, 기사 페이지
    headline = scrapy.Field()
    content = scrapy.Field()
    parent_link = scrapy.Field()
    article_link = scrapy.Field()
