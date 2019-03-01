# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# This Item class will work to collect all the individual manga page link
class MangaId(scrapy.Item):
    individual_manga_url = scrapy.Field()


# This Item will collect all the details from individual manga page
class MangaDetails(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    image = scrapy.Field()
    story_alternative = scrapy.Field()
    author = scrapy.Field()
    status = scrapy.Field()
    last_updated = scrapy.Field()
    view = scrapy.Field()
    genres = scrapy.Field()
    score = scrapy.Field()
    votes = scrapy.Field()
    summary = scrapy.Field()



# This Item will collect all the chapter from each manga page
class MangaChapterList(scrapy.Item):
    manga_id = scrapy.Field()
    chapter_id = scrapy.Field()
    full_chapter_url = scrapy.Field()
    chapter_link_text = scrapy.Field()
    chapter_view = scrapy.Field()
    chapter_time_uploaded = scrapy.Field()



#This Item will collect the ID of all related manga suggestion from chapter view page
class RelatedMangaSuggestionInChapterView(scrapy.Item):
    related_manga_suggestion_in_chapter_view = scrapy.Field()



# This Item will collect the popular manga list from front-page slider
class PopularMangaList(scrapy.Item):
    popular_manga_id = scrapy.Field()



# This Item will collect the most popular manga ID from front-page sidebar
class MostPopularMangaList(scrapy.Item):
    most_popular_manga_id_sidebar = scrapy.Field()



# This Item will collect the latest manga releases ID from front-page
class LatestMangaReleasesIdFrontPage(scrapy.Item):
    Latest_manga_releases_id_front_page = scrapy.Field()



# This Item will collect full image list from each manga chapter and will store with manga id
class MangaEachChapterImageListWithMangaId(scrapy.Item):
    manga_id = scrapy.Field()
    chapter_id = scrapy.Field()
    manga_each_chapter_image_list_with_manga_id = scrapy.Field()


# This spider will update daily to get all the update from front page
class UpdateSpider(scrapy.Item):
    popular_manga = scrapy.Field()
    latest_mange_releases = scrapy.Field()
    most_popular_manga = scrapy.Field()



# This spider will genres & categories
class GenresCategories(scrapy.Item):
    genres = scrapy.Field()
    categories = scrapy.Field()
