from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.get('http://www.baidu.com')
# ord=input('输入要搜索的内容：')
browser.find_element_by_id('kw').send_keys('风云')
browser.find_element_by_id('su').click()
time.sleep(2)
browser.find_element_by_class_name('n').click()