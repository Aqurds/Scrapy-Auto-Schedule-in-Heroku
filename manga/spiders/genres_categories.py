import scrapy
import json
from ..items import GenresCategories




# This spider will collect regularly all update manga id from front page
class my_first_scrapy(scrapy.Spider):
    name = 'genres_categories'

    start_urls = ['https://mangarock.herokuapp.com/']


    def parse(self, response):

        genres_categories = GenresCategories()


        genres_categories['genres'] = response.xpath('//ul[@class="tags tag-name"]/li/a/text()').extract()



        genres_categories['categories'] = response.xpath('//ul[@class="tags spec-tag"]/li/a/text()').extract()




        yield genres_categories

# Create genres_categories.json file
