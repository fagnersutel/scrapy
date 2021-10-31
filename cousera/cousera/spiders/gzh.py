import scrapy


class GzhSpider(scrapy.Spider):
    name = 'gzh'
    allowed_domains = ['clicrbs.com.br']
    start_urls = ['http://https://gauchazh.clicrbs.com.br/']

    def parse(self, response):
        self.log('Hello World! Scrapy Project')
