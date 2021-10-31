import scrapy


class UdacitySpider(scrapy.Spider):
    name = 'udacity'
    #allowed_domains = ['https://www.udacity.com/courses/all']
    start_urls = ['http://https://www.udacity.com/courses/all/']

    def parse(self, response):
        self.log('Crawler! Fagner Sutel')
        divs = response.xpath("/html/body/div[1]/div/div/div[2]/div")
        for div in divs:
            print(div)