# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class MangaPipeline(object):

    def __init__(self):
        # self.conn = pymongo.MongoClient(
        # 'localhost',
        # 27017
        # )
        #
        # db = self.conn['mangadb']
        # self.collection = db['manga_collection']

        self.connection = pymongo.MongoClient("ds159785-a0.mlab.com", 59785)
        self.db = self.connection["mangastuff"]
        self.db.authenticate("user", "2252010baby")
        # self.collection = db['test_auto_scraping']

    def process_item(self, item, spider):
		# self.collection = db['test_auto_scraping']
        # self.collection.insert(dict(item))
        if spider.name == 'manganame':
             self.db['manga_name_updater_list'].insert(dict(item))
             return item
        if spider.name == 'manga_details':
             self.db['all_manga_details'].insert(dict(item))
             return item
        if spider.name == 'manga_chapter_list':
             self.db['manga_chapter_updater_list'].insert(dict(item))
             return item
        if spider.name == 'manga_each_chapter_image_list_with_manga_id':
             self.db['manga_each_chapter_image_list_with_manga_id'].insert(dict(item))
             return item
        if spider.name == 'update_spider':
             self.db['update_spider'].insert(dict(item))
             return item
        return item
