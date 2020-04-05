# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class NewSpider(CrawlSpider):
    name = 'test11'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용 추천)
    # page=\d$ : 한자리
    # page=\d+ : 연속, follow=True
    rules = [
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline'),
    ]

    def parse_headline(self, response):
        # URL 로깅
        self.logger.info('Response URL : %s' % response.url)

        for m in response.css('ul.list_news2.list_allnews > li > div.cont_thumb'):
            # 헤드라인
            headline = m.css('strong > a::text').extract_first().strip()
            # 본문 20글자
            content = m.css('div.desc_thumb > span::text').extract_first().strip()

            yield {'headline': headline, 'content': content}



        print(response)
