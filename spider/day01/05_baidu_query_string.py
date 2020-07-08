from urllib import request
from urllib import parse

word=input('输入搜索内容')
url='https://www.sougou.com/tx?'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'}

query_string=parse.urlencode({'query':word})
url=url+query_string

req=request.Request(url=url,headers=headers)
res=request.urlopen(req)
html=res.read().decode('utf-8')

filename='{}.html'.format(word)
with open(filename,'w',encoding='utf-8') as f:
    f.write(html)
