from urllib import request
import time
import re
import csv
import random

class MaoyanSpider(object):
    def __init__(self):
        self.url="https://maoyan.com/board/4?offset={}"
        self.ua_list=[
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        ]

    def get_page(self,url):
        headers={'User-Agent':random.choice(self.ua_list)}
        req=request.Request(
            url=url,
            headers=headers
        )
        res=request.urlopen(req)
        html=res.read().decode('utf-8')

        self.parse_page(html)

    def parse_page(self,html):
        pattren=re.compile('',re.S)
        r_list=pattren.findall(html)
        self.write_page(r_list)

    def write_page(self,r_list):
        one_film_dict={}
        for rt in r_list:
            one_film_dict['name']=rt[0].strip()
            one_film_dict['star']=rt[1].strip()
            one_film_dict['time']=rt[2].strip()
            print(one_film_dict)

    def main(self):
        for offset in range(0,91,10):
            url=self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    start=time.time()
    spider=MaoyanSpider()
    spider.main()
    end=time.time()
    print('执行时间：%.2f' %(end-start))