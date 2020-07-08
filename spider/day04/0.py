from getIP import *
import requests
import random

url='http://httpbin.org/get'
headers={'User-Agent':'Mozilla/5.0'}
proxy_ip_list=get_ip_list()

def get_page(url):
    while True:
        if not proxy_ip_list:
            proxy_ip_list=get_ip_list()
        ip_port=random.choice(proxy_ip_list)
        proxies={
            'http':'http://{}'.format(ip_port),
            'https': 'https://{}'.format(ip_port),
        }
        try:
            html=requests.get(
                url=url,
                proxies=proxies,
                headers=headers,
                timeout=5
            ).text
            print(html)
            break
        except Exception as e:
            proxy_ip_list.remove(ip_port)
            continue

if __name__ == '__main__':
    print(get_ip_list())
