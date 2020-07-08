'''包装请求头，向httpbin.org发请求'''
from urllib import request

url='http://httpbin.org/get'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

#春节请求对象（包装请求） request
req=request.Request(url=url,headers=headers)
#发请求，获取响应对象
res=request.urlopen(req)
#读取内容
html=res.read().decode('utf-8')

print(html)