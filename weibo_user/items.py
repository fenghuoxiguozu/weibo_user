# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboUserItem(scrapy.Item):
    # define the fields for your item here like:
    user = scrapy.Field()
    fans_num = scrapy.Field()
    care_num = scrapy.Field()
    weibo_num = scrapy.Field()

