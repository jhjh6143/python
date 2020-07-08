from selenium import webdriver

options=webdriver.ChromeOptions()
options.add_argument('--headless')
browser=webdriver.Chrome(options=options)

browser=webdriver.Chrome()
browser.get('http://www.baidu.com')
browser.quit()