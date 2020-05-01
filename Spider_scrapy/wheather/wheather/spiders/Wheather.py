# -*- coding: utf-8 -*-
# 爬取中国各个城市的历史天气数据
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from ..items import WheatherItem
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class WheatherSpider(scrapy.Spider):
    '''
    start_requests，用selenium代替request
    parse，获取城市链接
    parse_month，获取各城市的各日期链接
    parse_final，爬
    '''
    name = 'Wheather'
    allowed_domains = ['www.aqistudy.cn']

    def start_requests(self): # 注意名字不要随意改！！！！！！
        start_urls = 'https://www.aqistudy.cn/historydata/'
        yield SeleniumRequest(url=start_urls, callback=self.parse)
    
    def parse(self, response):
        i=0
        citylink = LinkExtractor(restrict_xpaths='/html/body/div[3]/div/div[1]/div[2]/div[2]')
        citylinks = citylink.extract_links(response)  # 各个城市的天气数据链接   
        for cityurl in citylinks: 
            i+=1
            yield scrapy.Request(url=cityurl.url,meta={'i':i}, callback=self.parse_month)
    
    def parse_month(self, response):
        print(response.meta['i'])  # meta传递数值（对整体没有影响，作者自己看的）
        monthlink = LinkExtractor(restrict_xpaths='/html/body/div[3]/div[1]/div[2]/div[2]/div[2]')
        monthlinks = monthlink.extract_links(response)  # 每个城市各个月的天气数据链接
        for monthurl in monthlinks:
            if int(str(monthurl.url)[-6:]) == 201712:  # 简单起见，只选取了2017年12月的数据
                yield SeleniumRequest(url=monthurl.url,wait_time=4,wait_until=EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[1]/table/tbody/tr[29]/td[2]')),callback=self.parse_final)
    
    def parse_final(self,response):
        long = len(response.selector.xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr'))  # 计算每页一共这么多条
        dit = WheatherItem()
        # response.request.meta['driver'].current_url)[0]
        for line in range(2, long+1):
            dit['city'] = re.findall('(.+?)空气质量',response.selector.xpath('//*[@id="title"]/text()').extract_first())[0]
            dit['date'] = response.selector.xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr[%s]/td[1]/text()' % str(line)).extract_first()
            dit['quality'] = response.selector.xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr[%s]/td[3]/span/text()' % str(line)).extract_first()
            yield dit

# scrapy crawl somespider -s JOBDIR=crawls/somespider-1 （作者自己看的）