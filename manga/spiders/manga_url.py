import os
import scrapy
from ..items import MangaId





# This spider will extract all the individual manga page with pagination and store the links in managa_name.json file. With this file manga_details spider will extract all the details of each individual manga
class my_first_scrapy(scrapy.Spider):
    name = 'manganame'
    start_urls = [
        'https://mangarock.herokuapp.com/manga_list?type=latest&category=all&state=all&page=%s' % page for page in range(1,11)
    ]

    # DELETE the existing manga_name.json file and store the new data in a new manga_name.json file
    # json_file_name = 'manga_name.json'
    # if os.path.exists(json_file_name):
    #     os.remove(json_file_name)

    def parse(self, response):

        manga_url = MangaId()

        manga_url['individual_manga_url'] = response.xpath('//div[@class="list-truyen-item-wrap"]/h3/a/@href').getall()

        yield manga_url

# Create manga_name.json file
