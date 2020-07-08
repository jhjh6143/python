import requests
import time
import json
from threading import Thread
from queue import Queue

class XiaomiSpider(object):
    def __init__(self):
        self.url='http://app.mi.com/categotyAllListApi?page={}&categoryId=5&pageSize=30'
        self.headers={'User-Agent':'Mozilla/5.0'}
        self.url_queue=Queue()
        self.n=0

    def url_in(self):
        for i in range(67):
            url=self.url.format(i)
            self.url_queue.put(url)

    def get_data(self):
        while True:
            if self.url_queue.empty():
                break
            url=self.url_queue.get()
            html=requests.get(
                url=url,
                headers=self.headers
            ).content.decode('utf-8')
            html=json.loads(html)
            with open('xiaomi.json','a') as f:
                app_dict={}
                for app in html['data']:
                    app_dict['app_name']=app['displayName']
                    app_dict['app_link']='http://app.mi.com/details?id='+app['packageName']
                    self.n+=1
                    json.dump(app_dict,f,ensure_ascii=False)

    def main(self):
        self.url_in()
        t_list=[]
        for i in range(10):
            t=Thread(target=self.get_data)
            t_list.append(t)
            t.start()
        for i in t_list:
            i.join()
        print(self.n)

if __name__ == '__main__':
    start=time.time()
    spider=XiaomiSpider()

    spider.main()
    end=time.time()

    print(end-start)