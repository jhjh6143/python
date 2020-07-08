# -*- coding: utf-8 -*-
import scrapy


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://daomubiji.com/']

    def parse(self, response):
        pass
