# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def process_item(self, item, spider):
        return item


class MoviePipeline(object):
    def open_spider(self, spider):
        with open("my_meiju.txt", 'w') as fp:
            fp.write('123' + '\n')

    def process_item(self, item, spider):
        with open("my_meiju.txt", 'a') as fp:
            fp.write(item['name'] + '\n')
