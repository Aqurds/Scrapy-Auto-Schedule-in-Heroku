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

        self.connection = pymongo.MongoClient("ds249035.mlab.com", 49035)
        db = self.connection["aqurds"]
        db.authenticate("user", "2252010baby")
        self.collection = db['heroku_test_manga_details']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
