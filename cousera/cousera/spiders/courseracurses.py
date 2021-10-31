import scrapy


class CourseracursesSpider(scrapy.Spider):
    name = 'courseracurses'
    start_urls = ['https://www.coursera.org/browse?languages=pt']

    def parse(self, response):
        self.log('Hello World! Scrapy Project')