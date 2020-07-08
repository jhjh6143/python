import random
import time
import requests
from lxml import etree


class LianjiaSpider(object):
    def __init__(self):
        self.url="https://bj.lianjia.com/ershoufang/pg{}/"
        self.ua_list=[
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        ]

    def get_page(self,url):
        headers={'User-Agent':random.choice(self.ua_list)}
        res=requests.get(url,headers=headers)
        res.encoding='utf-8'
        html=res.text
        self.parse_page(html)

    def parse_page(self,html):
        parse_html=etree.HTML(html)
        li_list=parse_html.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"] |'
                                 ' //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"] ')
        house_dict={}
        for li in li_list:
            house_dict['house_name']=li.xpath('.//a[@data-el="region"]/text()')[0].strip()
            total_price=li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
            total_price=float(total_price)*10000
            house_dict['total_price']=total_price

            house_dict['unit_price']=li.xpath('.//div[@class="unitPrice"]/@data-price')[0].strip()
            print(house_dict)

    def main(self):
        for pg in range(1,5):
            url=self.url.format(pg)
            self.get_page(url)
            time.sleep(random.uniform(0,2))


if __name__ == '__main__':
    start=time.time()
    spider=LianjiaSpider()
    spider.main()
    end=time.time()
    print('执行时间：%.2f' %(end-start))