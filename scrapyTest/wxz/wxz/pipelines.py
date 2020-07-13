'''
@Author: hanchang
@LastModifiedBy: hanchang
'''
# -*- coding: utf-8 -*-

# Define your item pipelines here 对items里面提取的数据做进一步处理
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WxzPipeline(object):
    def process_item(self, item, spider):
        return item
