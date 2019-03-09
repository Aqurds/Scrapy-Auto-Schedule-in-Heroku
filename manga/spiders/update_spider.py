import scrapy
import json
from ..items import UpdateSpider




# This spider will collect regularly all update manga id from front page
class my_first_scrapy(scrapy.Spider):
    name = 'update_spider'

    start_urls = ['https://mangarock.herokuapp.com/']


    def parse(self, response):

        update = UpdateSpider()


        popular_manga_full_url = response.xpath('//div[@class="slide-caption"]/h3/a/@href').extract()
        popular_manga = []
        for id in popular_manga_full_url:
            popular_manga.append(id.split('/')[-1])
        update['popular_manga'] = popular_manga


        latest_manga_full_url = response.xpath('//a[@class="tooltip"]/@href').extract()
        latest_releases_manga = []
        for id in latest_manga_full_url:
            latest_releases_manga.append(id.split('/')[-1])
        update['latest_mange_releases'] = latest_releases_manga


        most_popular_manga_full_url = response.xpath('//div[@class="xem-nhieu-item"]/h3/a/@href').extract()
        most_popular_manga = []
        for id in most_popular_manga_full_url:
            most_popular_manga.append(id.split('/')[-1])
        update['most_popular_manga'] = most_popular_manga


        yield update

# Create update_spider.json file
