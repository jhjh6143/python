import requests

post_url='http://www.renren.com/PLogin.do'
get_url='http://www.renren.com/970294164/profile'
post_data={
    'email':'15110225726',
    'password':'zhanshen001'
}
headers={
    'User-Agent':'Mozilla/5.0(Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Referer':'http://www.renren.com/'
}
session=requests.session()
session.post(url=post_url,data=post_data,headers=headers)

html=session.get(url=get_url,headers=headers).text

print(html)