import requests
import time
import random
from hashlib import md5

#获取salt sign ts
def get_salt_sign_ts():
    ts=str(int(time.time()*1000))
    salt=ts+str(random.randint(0,9))
    string="fanyideskweb"+word+salt+"n%A-rKaT5fb[Gy?;N5@Tj"
    s=md5()
    s.update(string.encode())
    sign=s.hexdigest()
    return salt,ts,sign
def attack_yd():
    salt, ts, sign=get_salt_sign_ts(word)
    url=''
    headers={}
    data={}
    html_json=requests.post(
        url=url,
        headers=headers
    ).json()
    return html_json

if __name__ == '__main__':
    word=input('输入要翻译的单词')
    result=attack_yd(word)
    print(result)