# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Jobs(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    time_posted = scrapy.Field()


class Tenders(scrapy.Item):
    tender_code = scrapy.Field()
    tender_type = scrapy.Field()
    org_name = scrapy.Field()
    tender_title = scrapy.Field()
    tender_reference_no = scrapy.Field()
    publication_date = scrapy.Field()
    closing_date = scrapy.Field()
