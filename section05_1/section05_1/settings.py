# -*- coding: utf-8 -*-

# Scrapy settings for section05_1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'section05_1'

SPIDER_MODULES = ['section05_1.spiders']
NEWSPIDER_MODULE = 'section05_1.spiders'

# USER_AGENT
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 다운로드 간격
DOWNLOAD_DELAY = 2

# 쿠키 사용
COOKIES_ENABLED = True

# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
  'Referer': 'https://news.daum.net/',
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글쓰기(출력인코딩)
FEED_EXPORT_ENCODING = 'utf-8'

# 캐시사용
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
