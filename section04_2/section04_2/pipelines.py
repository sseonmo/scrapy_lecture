# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
# 파이프 라인 실습(1)
# 예) 잘못된 데이터 제거, DB저장, SNS 전송, SMS 전송, 메일 전송
class TestSpiderPipeline(object):
	# 최초 1회 실행
	def open_spider(self, spider):
		print('TestSpider Pipline Started.@@@@@@@@@@@@@@@@@@@@@@')
		spider.logger.info('TestSpider Pipline Started.@@@@@@@@@@@@@@@@@@@@@@')
		self.logger.info('TestSpider Pipline Started.@@@@@@@@@@@@@@@@@@@@@@')

	def process_item(self, item, spider):
		if int(item.get('rank_num')) < 11:
			item['is_pass'] = True
			return item
		else:
			raise DropItem(f'Dropped Item, Because This Site Rank is {item.get("rank_num")}')

	# 마지막 1회 실행
	def close_spider(self, spider):
		spider.logger.info('TestSpider Pipline Closed.@@@@@@@@@@@@@@@@@@@@@@')
		self.logger.info('TestSpider Pipline Closed.@@@@@@@@@@@@@@@@@@@@@@')
		print('TestSpider Pipline Closed.@@@@@@@@@@@@@@@@@@@@@@')
