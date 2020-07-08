from urllib import request
from urllib import parse

url='http://www.sougou.com/tx?'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}

query_string=parse.urlencode({'query':'美女'})
url=url+query_string+'&rsv_spt=1&rsv_iqid=0x80189fde000945a5&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=98010089_dg&ch=14&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug1=2&rsv_sug7=001&rsv_sug2=0&rsv_btype=i&inputT=1897&rsv_sug4=5215&rsv_sug=5'

req=request.Request(url=url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')

print(html)