# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import csv
import xlsxwriter
import os

# 파이프 라인 실습(2)
# 예) 잘못된 데이터 제거, DB저장, SNS 전송, SMS 전송, 메일 전송
class TestSpiderPipeline(object):
	# 초기화 메소드
	def __init__(self):
		# 엑셀 처리 선언
		xlsxFile = os.path.join(os.path.dirname(__file__), '..', 'result_excel.xlsx')
		self.workbook = xlsxwriter.Workbook(xlsxFile)
		# 워크시트
		self.worksheet = self.workbook.add_worksheet()
		# 삽입수
		self.rowcount = 1

		# CSV 처리선언 (a (append), w (write) )
		csvFile = os.path.join(os.path.dirname(__file__), '..', 'result.csv')
		self.csv_writer = csv.DictWriter(self.file_opener,
		                                 fieldnames=['rank_num', 'site_name', 'daily_time_site', 'daily_page_view',
		                                             'is_pass'])

	# 최초 1회 실행
	def open_spider(self, spider):
		spider.logger.info('TestSpider Pipline Started.@@@@@@@@@@@@@@@@@@@@@@')

	def process_item(self, item, spider):
		if int(item.get('rank_num')) < 41:
			item['is_pass'] = True
			# 엑셀저장, 첫번째 param - 열과 행번호 / 두번째 param - 데이터
			self.worksheet.write('A%s' % self.rowcount, item.get('rank_num'))  # item['rank_num'] / get으로 값을 가져와을때 값이 없으면 None, [''] 가져왔을때 값이 없으면 에러발생
			self.worksheet.write('B%s' % self.rowcount, item.get('site_name'))
			self.worksheet.write('C%s' % self.rowcount, item.get('daily_time_site'))
			self.worksheet.write('D%s' % self.rowcount, item.get('daily_page_view'))
			self.worksheet.write('E%s' % self.rowcount, item.get('is_pass'))
			self.rowcount += 1

			# CSV 저장
			self.csv_writer.writerow(item)

			return item
		else:
			raise DropItem(f'Dropped Item, Because This Site Rank is {item.get("rank_num")}')

	# 마지막 1회 실행
	def close_spider(self, spider):
		spider.logger.info('TestSpider Pipline Closed.@@@@@@@@@@@@@@@@@@@@@@')

		# 엑셀파일닫기
		self.workbook.close()
		# CSV 파일 닫기
		self.file_opener.close()
