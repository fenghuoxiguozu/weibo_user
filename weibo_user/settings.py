# -*- coding: utf-8 -*-

# Scrapy settings for weibo_user project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'weibo_user'

SPIDER_MODULES = ['weibo_user.spiders']
NEWSPIDER_MODULE = 'weibo_user.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo_user (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Origin": "https://login.sina.com.cn",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://login.sina.com.cn/signup/signin.php?entry=sso",
    "Accept-Encoding": "deflate, br",
    "Accept-Language": "en-GB,en;q=0.8,zh-CN;q=0.6,zh;q=0.4",
    'Cookie':'SINAGLOBAL=4973892408888.787.1499675528489; login_sid_t=b2f6bf25dc4193c82aa1f258126f6e67; cross_origin_proto=SSL; _s_tentry=www.baidu.com; Apache=8222847087292.115.1550061388515; ULV=1550061388520:48:4:3:8222847087292.115.1550061388515:1549974175872; UOR=,,login.sina.com.cn; un=17365355250@163.com; SCF=AvRwCuzeQLejicVUjAzyIOztp3Ii_A2TxlhvNFRSgAcA750R62bIQnb0BX1GR1eQgPeduran50FPFZJ5NCo7F1E.; SUHB=0mxU4eBSecyzUA; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5KTb89FaVd3XRyChE-y64e5JpV202Ne0qfe0-feo-7Bh2ceE4odcXt; SUB=_2AkMrOL39dcPxrAVRkPsQzWzgaolH-jyY7dQLAn7uJhMyAxgv7gcqqSVutBF-XGmqa5QJupYitymnhqxu5tDN2R1c',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibo_user.middlewares.WeiboUserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'weibo_user.middlewares.WeiboUserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'weibo_user.pipelines.MongdbPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


custom_settings = {
        "RANDOM_DELAY": 0.8,
        "DOWNLOADER_MIDDLEWARES": {
            "middlewares.random_delay_middleware.RandomDelayMiddleware": 100,
        }
    }


# MONGODB 主机名
MONGODB_HOST = "127.0.0.1"
# MONGODB 端口号
MONGODB_PORT = 27017
# 数据库名称
MONGODB_DBNAME = "weibo"
# 存放数据的表名称
MONGODB_SHEETNAME = "weibo_user"


USER_NAME='1058247664@qq.com'
USER_PASSWORD='lub0875357459in'


START_CRAWL_URL = 'https://weibo.com/sportschannel'
BASE_URL = 'https://weibo.com/p/{}/follow'
LOGIN_URL='https://login.sina.com.cn/sso/login.php?client=ssologin.js'
PASSWORD_URL = 'https://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=MTA1ODI0NzY2NCU0MHFxLmNvbQ%3D%3D&rsakt=mod&client=ssologin.js(v1.4.15)&_=1549695100663'