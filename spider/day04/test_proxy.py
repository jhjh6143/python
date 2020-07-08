import requests
url='http://httpbin.org/get'
proxy={
    'http':'http://149.129.126.235:8080',
    'https': 'https://149.129.126.235:8080',
}
print(requests.get(url,proxies=proxy).text)