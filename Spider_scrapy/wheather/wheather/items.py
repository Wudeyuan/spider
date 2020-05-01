# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WheatherItem(scrapy.Item):
    city = scrapy.Field(serializer=lambda x: x[8:])  # 城市
    date = scrapy.Field()  # 日期
    quality = scrapy.Field()  # 空气质量
    # location = scrapy.Field()  # 地点