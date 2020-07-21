# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# pylint: disable=import-error
import pymongo
import logging

from scrapy.exceptions import DropItem


class AnalyticsPipeline:

    def process_item(self, item, spider):
        return item


class MongoPipeline:

    collection_name = 'jobs'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        if hasattr(spider, 'collection_name'):
            self.collection_name = spider.collection_name

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if spider.name == 'tenders':
            self.db[self.collection_name].create_index([("tender_title", pymongo.TEXT)])
            if [item for item in self.db[self.collection_name].find( {"tender_code":item['tender_code']} ).limit(1)]:
                print("data already exist")

            else:
                self.db[self.collection_name].insert(dict(item))
                logging.debug("Post added to MongoDB")
                return item
        elif spider.name == "jobs" or spider.name == "linkedin":
            self.db[self.collection_name].insert(dict(item))
            logging.debug("Post added to MongoDB")
            return item
        else:
            self.db[self.collection_name].insert(dict(item))
            logging.debug("Post added to MongoDB")
            return item

