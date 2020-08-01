# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# pylint: disable=import-error
import scrapy


class Jobs(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    time_posted = scrapy.Field()
    reference = scrapy.Field()


class Tenders(scrapy.Item):
    tender_code = scrapy.Field()
    tender_type = scrapy.Field()
    org_name = scrapy.Field()
    tender_title = scrapy.Field()
    tender_reference_no = scrapy.Field()
    publication_date = scrapy.Field()
    closing_date = scrapy.Field()


class StockExchange(scrapy.Item):
    company = scrapy.Field()
    datetime_created = scrapy.Field()
    price = scrapy.Field()
    ltp = scrapy.Field()
    prev_price = scrapy.Field()
    today_open = scrapy.Field()
    today_high = scrapy.Field()
    today_low = scrapy.Field()
    turnover = scrapy.Field()
    volume = scrapy.Field()
    change = scrapy.Field()
    today_close = scrapy.Field()
