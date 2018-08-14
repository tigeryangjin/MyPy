# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def open_spider(self, spider):
        with open("douban_movie_top250.txt", 'w') as fp:
            fp.write('')

    def process_item(self, item, spider):
        with open('douban_movie_top250.txt', 'a') as f:
            f.write(item['rank'] + '	' + item['score'] + '	' + item['movie_name'] + '	' + item['url'] + '\n')
