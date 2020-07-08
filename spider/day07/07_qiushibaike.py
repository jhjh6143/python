from selenium import webdriver

browser=webdriver.Chrome()
browser.get('https://www.qiushibaike.com/text/')

# xpath='//div[@class="content"]/span'
# span=browser.find_element_by_xpath(xpath)
# print(span.text)
xpath='//div[@class="content"]'
div=browser.find_element_by_xpath(xpath)
print(div.text)