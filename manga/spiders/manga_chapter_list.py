import os
import scrapy
import json
import pymongo
from ..items import MangaChapterList




# This spider will use the individual manga url from the json file and will crawl each individual manga page and will collect all the chapter details
class my_first_scrapy(scrapy.Spider):
    name = 'manga_chapter_list'

    start_urls = []
    


    connection = pymongo.MongoClient("ds159785-a0.mlab.com", 59785)
    db = connection["mangastuff"]
    db.authenticate("user", "2252010baby")
    manga_link = db['manga_name_updater_list'].find()

    for item in manga_link:
        for url in item['individual_manga_url']:
            start_urls.append(url)


    def parse(self, response):

        manga_chapter_list = MangaChapterList()



        manga_chapter_list['manga_id'] = response.xpath('//div[@class="row"]/span[1]/a/@href')[0].extract().split('/')[-2]

        chapter_full_url = response.xpath('//div[@class="row"]/span[1]/a/@href').extract()
        chapter_id_list = []
        for id in chapter_full_url:
            chapter_id_list.append(id.split('/')[-1])
        manga_chapter_list['chapter_id'] = chapter_id_list

        manga_chapter_list['full_chapter_url'] = response.xpath('//div[@class="row"]/span[1]/a/@href').extract()
        manga_chapter_list['chapter_link_text'] = response.xpath('//div[@class="row"]/span[1]/a/text()').extract()
        # manga_chapter_list['chapter_view'] = response.xpath('//div[@class="row"]/span[2]/text()').extract()
        manga_chapter_list['chapter_time_uploaded'] = response.xpath('//div[@class="row"]/span[3]/text()').extract()



        yield manga_chapter_list

# Create manga_chapter_list.json file
