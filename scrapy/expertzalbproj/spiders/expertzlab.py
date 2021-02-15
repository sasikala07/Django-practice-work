import scrapy
from bs4 import BeautifulSoup as bs
from ..items import CourseItem
class ExpertzlabSpider(scrapy.Spider):
    name = 'expertzlab'
    allowed_domains = ['expertzlab.com']
    start_urls = ['http://expertzlab.com/']


    def parse(self, response):
        soup = bs(response.text)
        courses = soup.findAll('div', attrs={'class': 'course'})
        for course in courses:
            item = CourseItem()
            item['name'] = course.h4.a.text
            item['desc'] =course.ul   ###descriptions of each courses in ul
            item['duration'] = '6 months'
            yield  item
