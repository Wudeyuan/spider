# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



# 输出json...............
import json
class WheatherPipeline(object):
    def __init__(self):
        self.f = open('spdr.json', 'w+', encoding='utf-8')
    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.f.write(content)
        return item
    def close_spider(self, spider):
        self.f.close()