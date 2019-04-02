import os
import scrapy
import json
import pymongo
from ..items import MangaEachChapterImageListWithMangaId




# This spider will use each manga chapter url from the json file (manga_chapter_list.json) and will collect all image links with manga id
class my_first_scrapy(scrapy.Spider):
    name = 'manga_each_chapter_image_list_with_manga_id'

    start_urls = []
    


    connection = pymongo.MongoClient("ds159785-a0.mlab.com", 59785)
    db = connection["mangastuff"]
    db.authenticate("user", "2252010baby")
    manga_link = db['manga_chapter_updater_list'].find()

    for item in manga_link:
        for url in item['full_chapter_url']:
            start_urls.append(url)



    def parse(self, response):

        manga_chapter_url = MangaEachChapterImageListWithMangaId()



        manga_chapter_url['manga_id'] = response.xpath('//div[@class="vung-doc"]/img[1]/@src')[0].extract().split('/')[-3]

        manga_chapter_url['chapter_id'] = response.xpath('//div[@class="vung-doc"]/img[1]/@src')[0].extract().split('/')[-2]

        manga_chapter_url['manga_each_chapter_image_list_with_manga_id'] = response.xpath('//div[@class="vung-doc"]/img/@src').extract()


        yield manga_chapter_url

# Create manga_each_chapter_image_list_with_manga_id.json file
