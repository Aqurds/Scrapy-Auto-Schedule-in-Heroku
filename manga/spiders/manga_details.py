import os
import scrapy
import json
import pymongo
from ..items import MangaDetails




# This spider will use the individual manga url from the json file and will crawl each individual manga page and will collect all the details
class my_first_scrapy(scrapy.Spider):
    name = 'manga_details'

    start_urls = []
    

    connection = pymongo.MongoClient("ds159785-a0.mlab.com", 59785)
    db = connection["mangastuff"]
    db.authenticate("user", "2252010baby")
    manga_link = db['manga_name_updater_list'].find()

    for item in manga_link:
        for url in item['individual_manga_url']:
            start_urls.append(url)

    def parse(self, response):

        manga_details = MangaDetails()

        manga_details['id'] = response.url.split('/')[-1]
        manga_details['title'] = response.xpath('//div[@class="manga-info-top"]/ul/li/h1/text()')[0].extract()
        manga_details['image'] =response.xpath('//div[@class="manga-info-pic"]/img/@src')[0].extract()
        # manga_details['story_alternative'] = response.xpath('//span[@class="story-alternative"]/text()').extract()
        manga_details['story_alternative'] = response.xpath("//*[contains(@class, 'story-alternative')]/text()").extract()
        manga_details['author'] = response.xpath('//div[@class="manga-info-top"]/ul/li[2]/a/text()').extract()
        manga_details['status'] = response.xpath('//div[@class="manga-info-top"]/ul/li[3]/text()')[0].extract().split(' : ')[-1]
        manga_details['last_updated'] = response.xpath('//div[@class="manga-info-top"]/ul/li[4]/text()')[0].extract().split(' : ')[-1]
        # manga_details['view'] = response.xpath('//div[@class="manga-info-top"]/ul/li[6]/text()')[0].extract().split(' : ')[-1]
        manga_details['genres'] = response.xpath('//div[@class="manga-info-top"]/ul/li[7]/a/text()').extract()
        manga_details['score'] = response.xpath('//em[@id="rate_row_cmd"]/em/em[2]/em/em[1]/text()')[0].extract()
        manga_details['votes'] = response.xpath('//em[@id="rate_row_cmd"]/em/em[3]/text()')[0].extract()
        manga_details['summary'] = response.xpath('//div[@id="noidungm"]/text()')[1].extract().replace("\n", "")

        yield manga_details

# Create all_manga_details.json file
