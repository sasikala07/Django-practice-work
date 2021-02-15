import scrapy
from scrapy.loader import ItemLoader
from ..items import CourseItem
class TechehubSpider(scrapy.Spider):
    name = 'techehub'
    allowed_domains = ['techehub.com']
    start_urls = ['http://techehub.com/']
#another method usinh itemloader

    def parse(self, response):
        l = ItemLoader(item=CourseItem(), response=response)
        l.add_xpath("name", "//div[@class='fl-callout-content']/h3/span/a/text()")

        l.add_value("duration" , "Unknown") ##use extra value except xpath
        return l.load_item()