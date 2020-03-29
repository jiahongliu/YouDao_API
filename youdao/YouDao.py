import requests
from time import time
from random import randint
import hashlib
from flask import Flask

#定义一个函数复制md5加密
def hex5(value):
    mainp=hashlib.md5()
    mainp.update(value.encode('utf-8'))
    return mainp.hexdigest()

#定义一个有道翻译的类
class You_Dao_Translate(object):
    def __init__(self, word, salt, sign, ts):
        self.word = word
        self.salt = salt
        self.sign = sign
        self.ts = ts

    #定义一个返回翻译值的方法
    def got_translate(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1306594221@10.108.160.18; OUTFOX_SEARCH_USER_ID_NCOO=1132522992.2450435; JSESSIONID=aaaCdo-cHZGlkgKGUkRdx; ___rl__test__cookies=1584494074038',
            'Host': 'fanyi.youdao.com',
            'Referer': 'http://fanyi.youdao.com/',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'i': self.word,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': self.salt,
            'sign': self.sign,
            'ts': self.ts,
            'bv': '4aa7828b641c5e2587e46a4b35eb3523',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME',
        }
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        response = requests.post(url=url, data=data, headers=headers).json()
        return response['translateResult'][0][0]['tgt']

def run(word):
    ts = str(round(time() * 100))  # 获取时间戳取整
    salt = ts + str(randint(0, 9))  # ts末尾加上随机0-9数字
    sign_str = "fanyideskweb" + word + salt + "Nw(nmmbP%A-r6U3EUn]Aj"
    sign = hex5(value=sign_str)
    dd = You_Dao_Translate(word=word, ts=ts, salt=salt, sign=sign)
    return dd.got_translate()

if __name__ == '__main__':
    word = input('输入你要翻译的字:')
    a=run(word)
    print(a)

