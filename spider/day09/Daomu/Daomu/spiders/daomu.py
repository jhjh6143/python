# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        link_list=response.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        print(link_list)
        for link in link_list:
            yield scrapy.Request(
                url=link,
                callback=self.parse_two_html
            )
    def parse_two_html(self,response):
        article_list=response.xpath('//article')
        for article in article_list:
            item=DaomuItem()
            info_list=article.xpath('./a/text()').get().split()
            item['volume_name']=info_list[0]
            item['zh_num']=info_list[1]
            item['zh_name']=info_list[2]
            item['zh_link']=article.xpath('/a/@href').get()
            yield scrapy.Request(
                meta={'item':item},
                url=item['zh_link'],
                callback=self.parse_three_html
            )
    def parse_three_html(self,response):
        item=response.meta['item']
        content_list=response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['zh-content']='\n'.join(content_list)
        yield item