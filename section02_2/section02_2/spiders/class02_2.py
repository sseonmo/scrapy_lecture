# -*- coding: utf-8 -*-
import scrapy

class Class022Spider(scrapy.Spider):
	name = 'test3'
	allowed_domains = ['blog.scrapinghub.com']
	start_urls = ['https://blog.scrapinghub.com/']

	def parse(self, response):
		"""
		:param response:
		:return: request
		"""
		for url in response.css('div.post-item > div > a::attr("href")').getall():
			# url 바로 사용보다 urljoin 사용
			# urljoin 함수는 해당 url이 절대 경로가 아닐때 앞에 domain 정보를 붙여서 절대경로로 만들어 준다.
			yield scrapy.Request(response.urljoin(url), self.parse_title)

	def parse_title(self, response):
		"""
		상세페이지 -> 타이틀 추출
		:param response:
		:return: Text
		"""
		contents = response.css('div.post-body > span > p::text').extract()[:5]
		# print(contents)
		yield {'contents': ''.join(contents)}