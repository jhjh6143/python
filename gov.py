import requests
from lxml import etree
import pymysql
import re

class Goverment(object):
    def __init__(self):
        self.one_url='http://www.mca.gov.cn/article/sj/xzqh/2020/'
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
        self.db=pymysql.connect(
            'localhost','root','123456','govdb',charset='utf8'
        )
        self.cursor=self.db.cursor()

    def get_false_link(self):
        html=requests.get(
            url=self.one_url,
            headers=self.headers
        ).content.decode('utf-8','ignore')
        parse_html=etree.HTML(html)
        a_list=parse_html.xpath('//a[@class="artitlelist"]')
        for a in a_list:
            # title=a.xpath('./@title')[0]
            title=a.get('title')
            if re.findall('.*中华人民共和国县以上行政区划代码',title,re.S):
                two_false_link='http://www.mca.gov.cn'+a.get('href')
                return two_false_link

    def get_true_link(self):
        false_link=self.get_false_link()
        html=requests.get(url=false_link,headers=self.headers).text
        pattern=re.compile(r'window.location.href="(.*?)"',re.S)
        real_link=pattern.findall(html)[0]
        sel='select * from version WHERE link="{}"'.format(real_link)
        self.cursor.execute(sel)

        if self.cursor.fetchall():
            print('数据已是最新')
        else:
            self.get_data(real_link)
            ins='insert into version values(%s)'
            self.cursor.execute(ins,[real_link])
            self.db.commit()

    def get_data(self,real_link):
        html=requests.get(
            url=real_link,
            headers=self.headers
        ).text
        parse_html=etree.HTML(html)
        tr_list=parse_html.xpath('//tr[@height="19"]')
        print(tr_list)
        for tr in tr_list:
            code=tr.xpath('./td[2]/text()')[0]
            name=tr.xpath('./td[3]/text()')[0]
            print(name,code)

    def main(self):
        self.get_true_link()

if __name__ == '__main__':
    spider=Goverment()
    spider.main()