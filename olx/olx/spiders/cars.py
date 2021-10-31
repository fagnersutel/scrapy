# -*- coding: utf-8 -*-
import scrapy


class CarsSpider(scrapy.Spider):

    name = "cars"
    allowed_domains = ["pe.olx.com.br"]
    start_urls = ['http://pe.olx.com.br/veiculos/carros/']

    def parse(self, response):
        # items = response.xpath(
        #     '//ul[@id="main-ad-list"]/li[contains(@class, "item") and not(contains(@class, "list_native"))]'
        # )
        items = response.xpath(
            '//ul[@id="main-ad-list"]/li[not(contains(@class, "list_native"))]'
        )
        for item in items:
            url = item.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.xpath('//title/text()').extract_first()
        year = response.xpath(
            '//span[contains(text(), "Ano")]/following-sibling::strong/a/@title'
        ).extract_first()
        ports = response.xpath(
            '//span[contains(text(), "Portas")]/following-sibling::strong/text()'
        ).extract_first()
        yield {
            'title': title,
            'year': year,
            'ports': ports,
        }
