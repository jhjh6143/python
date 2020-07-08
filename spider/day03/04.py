import random
import time
import requests
from lxml import etree


class BaiduImageSpider(object):
    def __init__(self):
        self.ua_list=[
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        ]

    def get_tlink(self,url):
        headers={'User-Agent':random.choice(self.ua_list)}
        html=requests.get(url,headers=headers).content.decode('utf-8')
        parse_html=etree.HTML(html)
        print(parse_html)
        t_list=parse_html.xpath('//*[@id="thread_list"]/li//div[@class="t_concleafix"]/div/div/div/a/@href')
        for t in t_list:
            t_link='http//tieba.baidu.com'+t
            print(t_link)

if __name__ == '__main__':
    start=time.time()
    spider=BaiduImageSpider()
    spider.get_tlink('http://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96')
    end=time.time()
    print('执行时间：%.2f' %(end-start))