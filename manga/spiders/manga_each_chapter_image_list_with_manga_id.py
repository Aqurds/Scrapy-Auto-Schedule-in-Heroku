import scrapy
import json
from ..items import MangaEachChapterImageListWithMangaId




# This spider will use each manga chapter url from the json file (manga_chapter_list.json) and will collect all image links with manga id
class my_first_scrapy(scrapy.Spider):
    name = 'manga_each_chapter_image_list_with_manga_id'

    start_urls = []
    # chapter_id_dict = ''
    #
    # with open('manga_chapter_list.json', 'r') as f:
    #     chapter_id_dict = json.load(f)

    # for item in chapter_id_dict:
    #     for chapter_url in item['full_chapter_url']:
    #         start_urls.append(chapter_url)

    # # write the chapter list in a text file
    # with open('manga_chapter.txt', 'w') as f:
    #     for item in chapter_id_dict:
    #         for chapter_url in item['full_chapter_url']:
    #             f.write("'%s',\n" % chapter_url)

    def parse(self, response):

        manga_chapter_url = MangaEachChapterImageListWithMangaId()



        manga_chapter_url['manga_id'] = response.xpath('//div[@class="vung-doc"]/img[1]/@src')[0].extract().split('/')[-3]

        manga_chapter_url['chapter_id'] = response.xpath('//div[@class="vung-doc"]/img[1]/@src')[0].extract().split('/')[-2]

        manga_chapter_url['manga_each_chapter_image_list_with_manga_id'] = response.xpath('//div[@class="vung-doc"]/img/@src').extract()


        yield manga_chapter_url

# Create manga_each_chapter_image_list_with_manga_id.json file
