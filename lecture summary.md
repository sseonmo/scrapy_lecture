# scrapy

### scrapy project 생성
- scrapy startproject section01_2
- section01_2 > section01_2 로 디렉토리로 생성되어지고 기본파일들이 위치한다.  
![123](./images/startproject.png)

### scrapy spider 생성
- `scrapy 명령어는 scrapy.cfg 파일있는 디렉토리 이동후에 실행한다.`
- scrapy genspider [spider name] [crawling 할 url]
- crawling 연습하기 좋은 site -  https://blog.scrapinghub.com/
- domain 뒤에 `robots.txt` 을 붙여보면 허용되지 않은 경로를 알 수 있다. 
    >https://blog.scrapinghub.com/robots.txt


### 실행방법
1. scrapy crawl [spider name]
    > scrapy crawl test1
    > scrapy crawl test1 --nolog : 진행과정 생략하기 
1. scrapy runspider [created spider file ]
    > 주의사항 : spider file 있는 디렉토리로 이동 후 실행해야함  
    scrapy runspider testspider.py
    - crawl vs runspider
    > crawl 는 클로러를 완성 후 사용하는 게 좋고  
    runspider는 단위테스트처럼 기능을 추가 후 테스트 할 때 용이하다. (spider 하나하나 실행 시킬)
1. 실행옵션 - 결과 파일로 생성하기 
- scrapy crawl test2 -o result.jl -t jsonlines
- scrapy crawl test2 -o result.csv -t csv
    > --output=FILE , -o File : 파일명.확장자
    --output-format=FORMAT, -t FORMAT : 파일타입(json, jsonlines, jl, csv, xml, marshal, pickle)
    
### Scrapy Shell 활용하기
- 실행 : scrapy shell, scrapy shell <사이트 주소>
    > scrapy shell https://daum.net --set="ROBOTSTXT_OBEY=False"  
    --set 으로 settings의 설정을 그대로 적용해서 사용할 수 있다. 
- 대상 데이터 수집 테스트 ( css, xpath )
```
// 해당사이트의 정보를 받아온다. 
- fetch('https://blog.scrapinghub.com')
// fetch로 받아온 정보를 보여준다.
// css 나 xpath 를 테스트해 볼 수 있따. 
- response
- dir(response)
// fetch로 받아온 정보를 body의 값을 보여준다.
- response.body
// 기본 브라우저에 response 를 보여준다. 
- view(response)
```

### spider 활용
- domain mutil
- 사용환경 설정(spdier에 한정해서) 
- logger 사용
- response 분기

```python
# -*- coding: utf-8 -*-
import scrapy

# import 해서 logger 사용하는 방법
# import logging
# logger = logging.getLogger('Mylogger')

# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']
    # 실행방법 1
    # 멀티도메인
    start_urls = ['https://blog.scrapinghub.com/', 'https://naver.com', 'https://daum.net']

    # 사용자 시스템 설정 ( settings.py )
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'COOKIES_ENABLED': True,
    }
    # 실행방법2
    # Request 각각지정
    # def start_requests(self):
    #     yield scrapy.Request('http://blog.srapinghub.com/', self.parse1())
    #     yield scrapy.Request('htts://naver.com', self.parse2())
    #     yield scrapy.Request('https://daum.net', self.parse3())

    def parse1(self, response):
        pass

    def parse2(self, response):
        pass

    def parse3(self, response):
        pass

    def parse(self, response):
        # logger 사용
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response status : %s' % response.status)
        
        # response 분기 - 각각 도메인에 맞게 처리 
        if response.url.find('scrapinghub'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
```

 
### 유용한 것들
- response.urljoin
    >response.urljoin(url)  
     urljoin 함수는 해당 url이 절대경로가 아니라도 domain 정보를 붙여서 절대경로로 만들어 준다.  

### 주의사항
- settings.py 의 DOWNLOAD_DELAY 속성을 변경해야한다.
```python
"""
settings.py

# Obey robots.txt rules
# 사이트에서 크롤링을 허용하지 않는 곳은 하지 않겠다는 의미 
ROBOTSTXT_OBEY = False

- crawling 간격 / 1~2초 정도 권고함. 
- 너무 잦은 주기이면 blocking 당할 수 있다. 
"""
DOWNLOAD_DELAY = 1
```

