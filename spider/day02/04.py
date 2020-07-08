from urllib import request
import time
import re
import csv
import random
from useragent import ua_list

class MaoyanSpider(object):
    def __init__(self):
        self.url="https://maoyan.com/board/4?offset={}"

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

    # def write_page(self,r_list):
    #     one_film_dict={}
    #     for rt in r_list:
    #         one_film_dict['name']=rt[0].strip()
    #         one_film_dict['star']=rt[1].strip()
    #         one_film_dict['time']=rt[2].strip()
    #         print(one_film_dict)
    def write_page(self,r_list):
        with open('maoyan.csv','a',encoding='utf-8') as f:
            for rt in r_list:
                writer=csv.writer(f)
                writer.writerow(
                    [rt[0],rt[1].strip(),rt[2].strip()[5:15]]
                )


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