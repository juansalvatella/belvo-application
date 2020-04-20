# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Card(scrapy.Item):
    name = scrapy.Field()
    characteristics = scrapy.Field()
    more_info_url = scrapy.Field()
