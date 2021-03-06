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

### scrapy selector
- css(), xpath() / 둘다 혼합해서 사용가능함
- 참조사이트 
    > xpath 선택자 도움 사이트  
    https://docs.scrapy.org/en/latest/topics/selectors.html#working-with-xpaths  
    http://www.nextree.co.kr/p6278/
    
    > css 선택자 도움 사이트  
    https://docs.scrapy.org/en/latest/topics/selectors.html#extensions-to-css-selectors
    
```python
"""
- css 선택자
    A B : 자속
    A > B : 자식
    ::text -> 노드 텍스트만 추출
    ::attr(name) : 노드 소성 값 추출
    get(), getall() 사용숙지
    get(default='none') 사용 가능 : 값이 없을때 none 이 나옴
    example )
    response.css('title::text').get() : 타이틀 태그의 텍스트만 추출
    response.css('div > a:attr(href)').getall() : div 태그의 자식 a태그의 href 속성값을 전부 추

- Xpath 선택자
    nodename : 이름이 nodename 선택
    text() : 노드 텍스트만 추출
    / : 루트부터 시작
    // : 현재 node 부터 문서상의 모든 노드 조회
    . : 현재 node
    .. : 현재 노드의 부모노드
    @ 속성선택자
    extract(), extract_first() 사용숙지
    
    example )
    response.xpath('/div') : 루트 노드부터 모든 div 태그 선택
    response.xpath('//div[@id="id"]/a/text()').get() : div 태그 중 id가 'id'인 자식 a태그의 text 추출

- 중요
    get() == extract_first() / get_all() == extract()
    혼합사용 가능
    response.css('img').xpath('@src').getall()
"""
def parse(self, response):
    # 둘다 가능
    # response.css('nav#mySidenav > div a::text').getall()
    # response.xpath('//nav[@id="mySidenav"]/div/a/text()').extract()
    # 혼합 : response.css('nav#mySidenav').xpath('./div/a/text()').getall()
    # for n, text in enumerate(response.css('nav#mySidenav > div a::text').getall(), 1):
    for n, text in enumerate(response.xpath('//nav[@id="mySidenav"]/div//a/text()').extract(), 1):
        yield { 'num': n, 'learn Title': text }
```
 
### spdier items 활용
1. 데이터를 사전형(dict)로 관리, 오타 방지
1. 수집 데이터를 일관성있게 관리 가능
1. 추구 가공 및 DB 저장용이
```python
# items.py 
import scrapy

class ItArticle(scrapy.Item):
    # 타이틀, image url, 본문내용
    title = scrapy.Field()
    img_url = scrapy.Field()
    contents = scrapy.Field()
    
ㅡㅡㅡ

# spiders > spider.py
...
 
def parse_article(self, response):
    """
    :param response:
    :return: item
    """
    
    item = ItArticle()
    item['title'] = response.xpath('//header[@class="cat"]/h1/text()').extract_first()
    # item['img_url'] = response.xpath('//figure/img/@src').get()
    item['img_url'] = response.xpath('//img[@itemprop="contentUrl"]/@data-original').get()
    item['contents'] = ''.join(response.xpath('//div[@id="drr-container"]/p/text()').extract())
    
    self.logger.info(dict(item))
    
    yield item
...   
   
``` 

### Scrapy Export
- 출력형식, 저장위치 지정할 수 있다. 
- 실행방법 2가지
    - command execute
    - settings.py 설정으로 자동저장
     
```python
"""
- 출력형식
1.JSON, JSON Lines
2.CSV
3.XML, Pickle, Marshal

- 저장위치
1. Local File System
2. FTP - server
3. S3 - aws
4. standard console

- 방법 2가지
1. 커멘트 이용 : ( --output, -o), (--output-format, -t)
   옵션 설정 예) --set=FEED_EXPORT_INDENT=2
2. Settings.py 이용
   자동으로 저장(파이면, 형식, 위치 지정가능)
"""

# settings.py# 출력 (Export) 설정

# 파일이름 및 경로
# FEED_URI = 'result.json'
# FEED_URI = 'result.cav'
FEED_URI = 'result.jl'

# 파일형식
# FEED_FORMAT = 'json'
# FEED_FORMAT = 'csv'
FEED_FORMAT = 'jsonlines'

# 출력인코딩
FEED_EXPORT_ENCODING = 'utf-8'

# 기본 들려쓰기
FEED_EXPORT_INDENT = 1

# 저장소, 저장 형식 관련 레퍼런스
# 참조 - https://docs.scrapy.org/en/latest/topics/feed-exports.html#std:setting-FEED_STORAGE_FTP_ACTIVE

```

### Scrapy 환경설정
1. 커맨드 라인 실행 -> scrapy crawl 클로러명 -s(--set) <NAME>=<VALUE>
1. Spider 실행시 직접 지정
1. 사용자 시스템 설정 ( settings.py )
    > custom_settings = {  
      'DOWNLOAD_DELAY': 1,  
      'COOKIES_ENABLED': True,  
      }
1. Settings.py에 지정 -> 추천
1. 서브 명령어(신경x)
1. 클로벌 설정 : scrapy.settings.defalut_settings
- [settings.py 설정설명](section04_1/section04_1/settings.py)

### Scrapy Pipeline
- 잘못된 데이터 제거, DB저장, SNS 전송, SMS 전송, 메일 전송 
- open_spider : pipeline 시작시 최초 1회 실행(파일을 열거나, DB 연결을 하거나 등등..) 
    > __init__ 를 대체로 사용할 수 있음
- process_item : 실질적인것을 처리하는 곳 ( db저장, 엑셀저장, email, sns 등등..)
- close_spider : pipeline 종료 1회 실행(종료작업, 파일종료하거나 DB를 commit 하는 등등)
- [참조1](section04_2/section04_2/pipelines.py), [참조2](section04_2/section04_3/pipelines.py)

### 유용한 것들
- response.urljoin
    >response.urljoin(url)  
     urljoin 함수는 해당 url이 절대경로가 아니라도 domain 정보를 붙여서 절대경로로 만들어 준다.  

- 엑셀로 파일저장 Package
    > pip install xlsxwriter

- [user agent fake middleward](https://github.com/alecxe/scrapy-fake-useragent)
    > pip install scrapy-fake-useragent  
    
        
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


