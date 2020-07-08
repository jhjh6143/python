import time
import requests
from lxml import etree
import random

class DoubanSpider(object):
    def __init__(self):
        self.url="https://movie.douban.com/j/chart/top_list" \
                 "type={}&interval_id=100%A90&action=&" \
                 "start=0&limit={}"
        self.headers={
        'Accept':'*/*',
        'Accept-Language':'zh-CN,zh;=0.9',
        'Connectiom':'keep-alive',
         'Cookie':'movie.douban.com',
         'Referer':'https://movie.douban.com/typerank?ty',
         'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
         'X-Requested-With':'XMLhttpRequest',}

    def get_film_info(self,url):
        html_json=requests.get(
            url=url,
            headers=self.headers
        ).json()
        for film in html_json:
            name=film['title']
            score=film['score']
            print(name,score)

    def main(self):
        type_dict={'剧情':'11','喜剧':'24','爱情':'13'}
        film_type=input('输入电影类型(剧情|喜剧|爱情)')
        if film_type in type_dict:
            limit=input('请输入电影数量：')
            ty=type_dict[film_type]
            url=self.url.format(ty,limit)
            self.get_film_info(url)
        else:
            print('类型不存在')

if __name__ == '__main__':
    start=time.time()
    spider=DoubanSpider()
    spider.main()
    end=time.time()
    print('执行时间：%.2f' %(end-start))