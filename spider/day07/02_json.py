import json

app_info={'营业名称':'呵呵礼拜','link':'http://hehe.com'}

with open('xiaomi.json','a') as f:
    json.dump(app_info,f,ensure_ascii=False)