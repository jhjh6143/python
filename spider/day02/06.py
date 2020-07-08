from urllib import request
import time
import re
import csv
import random
import pymysql
from useragent import *

class FilmSky(object):
    def __init__(self):
        self.url='https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

        self.db=pymysql.connect(
            '127.0.0.1','root','123456','maoyandb',charset='utf8'
        )
        self.cursor=self.db.cursor()


    def get_page(self,url):
        req=request.Request(
            url=url,
            headers={'User-Agent':random.choice(ua_list)}
        )
        res=request.urlopen(req)
        html=res.read().decode('gbk','ignore')

        return html

    def parse_page(self,html):
        pattern=re.compile('<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?>(.*?)</a>',re.S)
        film_list=pattern.findall(html)
        # print(film_list)
        ins='insert into filmsky VALUES (%s,%s)'
        for film in film_list:
            film_name=film[1]
            film_link='https://www.dytt8.net'+film[0]
            download_link=self.parse_two_html(film_link)
            self.cursor.execute(ins,[film_name,film_link])
            self.db.commit()
            d={
                '电影名称':film_name,
                '下载链接':download_link
            }
            print(d)

    def parse_two_html(self,film_link):
        two_html=self.get_page(film_link)
        pattern=re.compile('<td style="WORD-WRAP.*?>.*?>(.*?)</a>',re.S)
        download_link=pattern.findall(two_html)[0]

        return download_link

    def main(self):
        for page in range(1,11):
            url=self.url.format(page)
            html=self.get_page(url)
            self.parse_page(html)
            time.sleep(random.randint(1,3))
            print('第%d页成功'% page)

if __name__ == '__main__':
    start=time.time()
    spider=FilmSky()
    spider.main()
    end=time.time()
    print('执行时间 ：%.2f '%(end-start))