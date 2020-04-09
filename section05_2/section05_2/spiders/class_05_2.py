# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItems

# 페이지 + 상세 페이지 크롤링 추가
# 미들웨어 설치 : pip install scrapy_fake_useragent
class NewSpider(CrawlSpider):
	name = 'test12'
	allowed_domains = ['news.daum.net', 'news.v.daum.net']
	start_urls = ['https://news.daum.net/breakingnews/digital']

	# 링크 크롤링 규칙(정규표현식 사용 추천)
	# page=\d$ : 한자리
	# page=\d+ : 연속, follow=True
	rules = [
		Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_parent'),
	]

	def parse_parent(self, response):
		# 부모 URL 로깅
		self.logger.info('Parent Response URL : %s' % response.url)

		for url in response.css('ul.list_news2.list_allnews > li > div.cont_thumb'):
			# URL 신문기사
			article_url = url.css('strong > a::attr(href)').get().strip().replace('v.daum.net', 'news.v.daum.net')
			self.logger.info('child article URL : %s' % article_url)
			# 요청
			yield scrapy.Request(article_url,  callback=self.parse_child, meta={'parent_url': response.url},  cb_kwargs=dict(parent_url=response.url))

	def parse_child(self, response, parent_url):
		# 부모, 자식 수신 정보 로깅
		# self.logger.info('---------------------------------------------------')
		# print(parent_url)
		# self.logger.info('meta : Response From Parent URL : %s' % response.meta.get('parent_url'))
		# self.logger.info('cb_kwargs : Response From Parent URL : %s' % parent_url)
		# self.logger.info('Child Response URL : %s' % response.url)
		# self.logger.info('Child Response Status : %s' % response.status)
		# self.logger.info('---------------------------------------------------')

		article = ArticleItems()

		# 헤드라인
		headline = response.css('h3.tit_view::text').extract_first().strip()
		# 본문
		# 리스트 -> 문자열 변경
		c_list = response.css('div.article_view > section > p::text').extract_first()
		content = ''.join(c_list).strip()

		yield ArticleItems(headline=headline, content=content, parent_link=parent_url, article_link=response.url)
