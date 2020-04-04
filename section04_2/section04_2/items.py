# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SiteRankItems(scrapy.Item):
    # 제목, 사이트 이름, 머문 시간, 페이지뷰, 파이프라인 통과 여부
    rank_num = scrapy.Field()
    site_name = scrapy.Field()
    daily_time_site = scrapy.Field()
    daily_page_view = scrapy.Field()
    is_pass = scrapy.Field()