import requests
import re
import execjs

class BadiduTrnslateSpider(object):
    def __init__(self):
        self.get_url='https://fanyi.baidu.com/?aldtype=16047'
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.",
            "accept - encoding": "gzip, deflate, br",
            "accept - language": "zh - CN, zh;q = 0.9",
            "cache-control": "max-age=0",
            "cookie": "PSTM=1587085494; BAIDUID=2196C1B3137896FDE7F0328311089ABB:FG=1; BIDUPSID=1894C2FC21ED5B2316EB4AD9BB1F9002; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-264%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[S_ukKV6dOkf]=mk3SLVN4HKm; delPer=0; PSINO=1; H_PS_PSSID=1454_31672_21093; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1592283842,1592283994,1592284465,1592285780; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1592288363; __yjsv5_shitong=1.0_7_1f72a0419902b6c04a0ec599cab71a0de464_300_1592288388098_111.49.78.4_4c98f411; yjs_js_security_passport=21af47cc79e259eb1c3b48758f54bdef47cc35b7_1592288390_js",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400}",
        }

    def get_token(self):
        html=requests.get(
            url=self.get_url,
            headers=self.headers
        ).text
        #正则解析
        pattern=re.compile("token: '(.*?)',",re.S)
        token=pattern.findall(html)[0]
        return token

    def get_sign(self,word):
        with open('01.js','r') as f:
            js_data=f.read()
        execjs_obj=execjs.compile(js_data)
        sign=execjs_obj.eval('e("{}")'.format(word))
        return sign

    #获得翻译结果
    def get_result(self,word,fro,to):
        token=self.get_token()
        sign=self.get_sign(word)
        formdata={
        "from": fro,
        "to": to,
        "query": word,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign":sign,
        "token":token,
        }
        html_json=requests.post(
            url='https://fanyi.baidu.com/v2transapi',
            data=formdata,
            headers=self.headers
        ).json()
        result=html_json['trans_result']['data'][0]['dst']
        return result
if __name__ == '__main__':
    spider=BadiduTrnslateSpider()
    choice=input("1.翻译英语 2.翻译汉语 请选择（1/2）")
    if choice=='1':
        fro='en',
        to='zh'
    else:
        fro='zh'
        to='en'
    word=input('请输入要翻译的单词')
    result=spider.get_result(word,fro,to)
    print(result)