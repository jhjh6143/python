import requests

def get_ip_list():
    api_url=""
    html=requests.get(url=api_url).text+'192.168.1.3:80'
    ip_port_list=html.split('\r\n')
    return ip_port_list

if __name__ == '__main__':
    print(get_ip_list())