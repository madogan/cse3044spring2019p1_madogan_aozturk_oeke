# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilimFii(scrapy.Item):
    source = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
