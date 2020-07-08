import requests

url='http://imgm.gmw.cn/attachement/jpg/site2/20161022/3045424595179290786.jpg'

headers={'User-Agent':'Mozilla/5.0'}

html=requests.get(url,headers=headers).content

with open('赵丽颖.jpg','wb') as f:
    f.write(html)
