# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobAddress = scrapy.Field()
    jobSalary = scrapy.Field()
    jobEducation = scrapy.Field()
    jobWorkYear = scrapy.Field()
    jobCom = scrapy.Field()
    jobKey = scrapy.Field()
    pass
