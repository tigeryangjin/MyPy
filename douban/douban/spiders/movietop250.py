# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider
from douban.items import MovieTop250Item


# scrapy crawl douban_movie_top250 -o douban.csv

class DoubanMovieTop250Spider(Spider):
    name = 'douban_movie_top250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for each_movie in movies:
            item = MovieTop250Item()
            item['url'] = \
                each_movie.xpath('./div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/@href').extract()[0]
            item['rank'] = each_movie.xpath('./div[@class="item"]/div[@class="pic"]/em[@class=""]/text()').extract()[0]
            item['movie_name'] = \
                each_movie.xpath(
                    './div[@class="item"]/div[@class="info"]/div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['score'] = \
                each_movie.xpath(
                    './div[@class="item"]/div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()[
                    0]

            yield item

        # 获取当前url的下一页链接
        next_page = response.xpath('//span[@class="next"]/a/@href').extract_first()
        # print(next_page)

        if next_page:
            request_url = response.urljoin(next_page)
            print(request_url)
            yield Request(request_url, callback=self.parse)
