# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlsxwriter
import os

class Section052Pipeline(object):
    def process_item(self, item, spider):
        return item

    def __init__(self):
        # 엑셀 처리 선언
        xlsxFile = os.path.join(os.path.dirname(__file__), '..', 'result_excel.xlsx')
        self.workbook = xlsxwriter.Workbook(xlsxFile)
        # 워크시트
        self.worksheet = self.workbook.add_worksheet()
        # 삽입수
        self.rowcount = 2
        self.worksheet.write('A1', '헤드라인')
        self.worksheet.write('B1', 'content')
        self.worksheet.write('C1', '부모url')
        self.worksheet.write('D1', '자식url')

    def process_item(self, item, spider):
        spider.logger.info("====== process_item ======")
        # 엑셀저장, 첫번째 param - 열과 행번호 / 두번째 param - 데이터
        self.worksheet.write('A%s' % self.rowcount, item.get('headline'))
        self.worksheet.write('B%s' % self.rowcount, item.get('content'))
        self.worksheet.write('C%s' % self.rowcount, item.get('parent_link'))
        self.worksheet.write('D%s' % self.rowcount, item.get('article_link'))
        self.rowcount += 1

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('TestSpider Pipline Closed.@@@@@@@@@@@@@@@@@@@@@@')

        # 엑셀파일닫기
        self.workbook.close()