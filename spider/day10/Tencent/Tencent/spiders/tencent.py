# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1592105619669&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1591347751739&postId={}&language=zh-cn'

    start_urls = [one_url.format(1)]


    def parse(self, response):
        for page_index in range(1,51):
            url=self.one_url.format(page_index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one
            )
    def parse_one(self, response):
        html=json.loads(response.text)
        for job in html['Data']['Posts']:
            item=TencentItem()
            item['zh_name']=job['RecruitPostName']
            item['zh_type']=job['CategoryName']
            post_id=job['PostId']
            two_url =self.two_url.format(post_id)
            yield scrapy.Request(
                url=two_url,
                meta={'item':item},
                callback=self.parse_two
            )
    def parse_two(self, response):
        item =response.meta['item']
        html=json.loads(response.text)
        item['zh_duty']=html['Data']['Responsibility']
        item['zh_require']=html['Data']['Requirement']
        yield item


