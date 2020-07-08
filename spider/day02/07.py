import requests

# url='http://httpbin.org/get'
url='http://www.baidu.com'
headers={'User-Agent':'xxxxxxxxxxxxxxxxx'}

html=requests.get(url,headers=headers).text
res=requests.get(url,headers=headers)
res.encoding='gbk'
print(res.content)
print(res.status_code)
print(res.url)