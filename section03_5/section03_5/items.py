# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Scrapy Item
# 장점
# 1. 수집 데이터를 일관성있게 관리 가능
# 2. 데이터를 사전형(dict)로 관리, 오타 방지
# 3. 추구 가공 및 DB 저장용이

import scrapy


class ItArticle(scrapy.Item):
    # 타이틀, image url, 본문내용
    title = scrapy.Field()
    img_url = scrapy.Field()
    contents = scrapy.Field()