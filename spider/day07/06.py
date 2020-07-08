from selenium import webdriver

browser=webdriver.Chrome()
browser.get('http://www.baidu.com')


html=browser.page_source
result=browser.page_source.find('su')
print(result)