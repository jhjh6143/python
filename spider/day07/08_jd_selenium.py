from selenium import webdriver
import time
class JdSpider(object):
    def __init__(self):
        self.browser=webdriver.Chrome()
        self.url='https://www.jd.com/'
        self.i=0

    def get_page(self):
        self.browser.get(self.url)
        self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('水果')
        self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
        time.sleep(2)

    def parse_page(self):
        self.browser.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)
        li_list=self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
        for li in li_list:
            info=li.text.split('\n')
            if info[0].startswith('每满'):
                price=info[1]
                name=info[2]
                number=info[3]
                market=info[4]
            elif info[0]=='单件':
                price=info[3]
                name=info[4]
                number=info[5]
                market=info[6]
            elif info[0].startswith('￥') and info[1].startswith('￥'):
                price=info[0]
                name=info[2]
                number=info[3]
                market=info[4]
            else:
                price=info[0]
                name=info[1]
                number=info[2]
                market=info[3]
            print(price,name,number,market)
            self.i+=1

    def main(self):
        self.get_page()
        while True:
            self.parse_page()
            if self.browser.page_source.find('pn-next disabled')==-1:
                self.browser.find_element_by_class_name('pn-next').click()
                time.sleep(3)
            else:
                break
        print(self.i)
if __name__ == '__main__':
    spider=JdSpider()
    spider.main()