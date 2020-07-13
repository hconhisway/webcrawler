'''
@Author: hanchang
@LastModifiedBy: hanchang
'''
# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('F:\webcrawler\webcrawler\scrapyTest\wxz\wxz')
from items import WxzItem

class NovelSpiderSpider(scrapy.Spider):
    name = 'novel_spider'
    allowed_domains = ['aixiawx']
    start_urls = ['http://aixiawx.com/16/16039/10137185.html']

    def parse(self, response):
        #print ("dfdg")

        #data=response.xpath('//div[@id="content"]/text()').extract()
        #print (data)

        item = WxzItem()
        item['title']=response.xpath("/html/head/title/text()").extract()[0]
        item['content'] = response.xpath('//div[@id="content"]/text()').extract()

        yield item

