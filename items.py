# -*- coding: utf-8 -*-

import scrapy


class CensusItem(scrapy.Item):
    district = scrapy.Field()
    state = scrapy.Field()
