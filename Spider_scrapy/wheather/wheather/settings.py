# -*- coding: utf-8 -*-

# Scrapy settings for wheather project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wheather'

SPIDER_MODULES = ['wheather.spiders']
NEWSPIDER_MODULE = 'wheather.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wheather (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wheather.middlewares.WheatherSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wheather.middlewares.WheatherDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wheather.pipelines.WheatherPipeline': 300,
#}

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

#..............................................
# 改为False
ROBOTSTXT_OBEY = False

# 加代理
USER_AGENT ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36' 

# log级别设为warning
LOG_LEVEL='WARNING' 

# 导出json
ITEM_PIPELINES = {
   'wheather.pipelines.WheatherPipeline': 300,
}

# 涉及到动态加载，该案例用scrapy-selenium包来嫁接scrapy和selenium。
# 网上有不少教程自己写中间件来引入selenium，可以但是没有必要！！！
DOWNLOADER_MIDDLEWARES  = {
     'scrapy_selenium.SeleniumMiddleware':800
}

# selenium设置
SELENIUM_DRIVER_NAME= 'chrome'  # 用chromedriver
SELENIUM_DRIVER_EXECUTABLE_PATH = r"C:/Anaconda3/chromedriver.exe"
SELENIUM_DRIVER_ARGUMENTS = ['--headless',]  # '--start-maximized'
# 原包不提供无图模式，该案例对包的代码进行了修改
# 若不需要无图模式，可忽略余下部分
SELENIUM_DRIVER_EXP_ARGUMENTS=[{"profile.managed_default_content_settings.images": 2}] 
# 修改部分如下
'''
browser_executable_path,driver_exp_arguments):  #.........wdy
or exp_argument in driver_exp_arguments: #..................... wdy
     driver_options.add_experimental_option("prefs", exp_argument) # ...wdy
driver_exp_arguments = crawler.settings.get('SELENIUM_DRIVER_EXP_ARGUMENTS')  #...............wdy
driver_exp_arguments=driver_exp_arguments #............wdy
'''