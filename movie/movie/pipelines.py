# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def open_spider(self, spider):
        with open("download/my_meiju.txt", 'w') as fp:
            fp.write('')

    def process_item(self, item, spider):
        with open("download/my_meiju.txt", 'a') as fp:
            fp.write(item['ranking'] + ',' + item['name'] + ',' + item['url'] + '\n')
            # fp.write(item['name'] + ',' + item['url'] + '\n')
