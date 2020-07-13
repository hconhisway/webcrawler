'''
@Author: hanchang
@LastModifiedBy: hanchang
'''
# -*- coding: utf-8 -*-

# Define here the models for your scraped items  数据结构定义文件
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WxzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    pass
