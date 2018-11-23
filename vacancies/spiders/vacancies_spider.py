import scrapy
import json
from sys import getdefaultencoding

class VacanciesSpider(scrapy.Spider):
    name = 'vacancies'

    start_urls = ['https://rostov.hh.ru/vacancies/programmist']

    def parse(self, response):
        for item in response.css('.vacancy-serp-item'):
            yield {
                'vacancy-name': item.css('.search-item-name a::text').extract_first(),
                'salary': item.css('.vacancy-serp-item__compensation::text').extract_first(),
                'link': item.css('.search-item-name a::attr(href)').extract_first()
            }
        for href in response.css('.bloko-button.HH-Pager-Controls-Next.HH-Pager-Control::attr(href)'):
            yield response.follow(href, callback=self.parse)
