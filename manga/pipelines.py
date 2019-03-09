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
        db = self.connection["mangastuff"]
        db.authenticate("user", "2252010baby")
        self.collection = db['genres_categories']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
