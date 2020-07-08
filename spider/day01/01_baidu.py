#导入模块
import urllib.request

# url='http://www.baidu.com/'
url='http://httpbin.org/get'
#向白带多发请求
response=urllib.request.urlopen(url)
#获取响应对象内容
print(response.read().decode('utf-8'))
#
# print(response.getcode())
#
# print(response.geturl())