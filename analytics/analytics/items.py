# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnalyticsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Jobs(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    time_posted = scrapy.Field()
