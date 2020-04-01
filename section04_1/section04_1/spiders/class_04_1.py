# -*- coding: utf-8 -*-
import scrapy

# Scrapy 환경설정
# 중요

# 실행방법
# 1. 커맨드 라인 실행 -> scrapy crawl 클로러명 -s(--set) <NAME>=<VALUE>
# 2. Spider 실행시 직접 지정
    # 사용자 시스템 설정 ( settings.py )
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 1,
    #     'COOKIES_ENABLED': True,
    # }
# 3. Settings.py에 지정 -> 추천
# 4. 서브 명령어(신경x)
# 5. 클로벌 설정 : scrapy.settings.defalut_settings



class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    def parse(self, response):
        for idx, title in enumerate(response.css('div.post-excerpt-container > h3 > a::attr(title)').getall(), 1):
            self.logger.info("{} | {}".format(str(idx), title))
            # yield dict(num=idx, headline=title)
            yield {
                'num': idx
                , 'headline': title
            }


