# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline:
    def process_item(self, item, spider):
        print(item['name'])
        print(item['star'])
        print(item['time'])

        return item

class MaoyanMysqlPipeline:
    def process_item(self, item, spider):
        return item
