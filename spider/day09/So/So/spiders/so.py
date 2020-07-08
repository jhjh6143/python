# -*- coding: utf-8 -*-
import scrapy
import json
from  ..items import SoItem
class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    def start_requests(self):
        url='http://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
        for i in range(5):
            sn=i*30
            full_url=url.format(sn)
            yield scrapy.Request(
                url=full_url,
                callback=self.parse_image
            )
    def parse_image(self, response):
        html=json.loads(response.text)
        for img in html['list']:
            item=SoItem()
            item['img_link']=img['qhimg_url']
            yield item