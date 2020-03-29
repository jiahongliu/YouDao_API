import requests

url='http://127.0.0.1:5000/test?word='
word='美女'
url+=word
print(requests.get(url).text)
