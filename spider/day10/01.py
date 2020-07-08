from selenium import webdriver
from PIL import Image


options=webdriver.ChromeOptions()
# options.add_argument('windows-size=1900x3000')
browser = webdriver.Chrome(options=options)
def get_screen_shot():
    browser.get("http://www.yundama.com")
    browser.save_screenshot('index.png')
def get_caphe():
    localtion=browser.find_element_by_xpath('//*[@id="verifyImg"]').location
    size=browser.find_element_by_xpath('verifyImg').size
    left=localtion['x']
    top=localtion['y']
    right=left+size['width']
    bottom=top+size['height']
    img=Image.open('index.png').crop()
    img.save('verify.png')
    return img

    # result=get_result('verify.png')
    # return result
if __name__ == '__main__':
    get_screen_shot()
    result=get_caphe()
    print(result)