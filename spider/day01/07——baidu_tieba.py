import random
from urllib import request,parse

import time


class BaiduSpider(object):
    def __init__(self):
        self.url='http://tieba.baidu.com/f?kw={}&pn={}'
        self.headers={'User-Agent':'Mozilla/5.0'}

    def get_page(self, url,):
        req=request.Request(url=url,headers=self.headers)
        res=request.urlopen(req)
        html=res.read().decode('utf-8')

        return html

    def parse_page(self):
        pass

    def write_page(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    def main(self):
        name=input('请输入贴吧名')
        start=int(input('请输入起始页'))
        end=int(input('请输入终止页'))
        for page in range(start,end+1):
            pn=(page-1)*50
            kw=parse.quote(name)
            url=self.url.format(kw,pn)
            html=self.get_page(url)
            filename='{}-第{}页.html'.format(name,page)
            self.write_page(filename,html)
            print('第{}页爬成功'.format(page))
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    spider=BaiduSpider()
    spider.main()