# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JKNiuNaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    shop_name = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    price_plus = scrapy.Field()
    commentcount = scrapy.Field()
    videocount = scrapy.Field()
    aftercount = scrapy.Field()
    goodcount = scrapy.Field()
    generalcount = scrapy.Field()
    poorcount = scrapy.Field()

