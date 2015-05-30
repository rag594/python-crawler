import scrapy
from tutorial.items import *
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class CensusSpider(CrawlSpider):
    name = 'census2011'
    allowed_domains = ['census2011.co.in']
    start_urls = ['http://www.census2011.co.in/district.php']
    rules = [Rule(LinkExtractor(allow = ['/district.php']), 'parse_census')]

    def parse_census(self, response):
        census = CensusItem()
        census['district'] = response.xpath("//div[@class = 'table']//div[@class = 'row']//a[@title]//text()").extract()
        census['state'] = response.xpath("//div[@class = 'table']//div[@class = 'row']//div[@class = 'cell mhide']//b//a/text()").extract()
        return census
