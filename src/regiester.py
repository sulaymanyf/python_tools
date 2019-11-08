import requests

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'accept': '*/*',
    'Origin': 'http://172.16.6.107:7001',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'DNT': '1',
    'Content-Type': 'application/json',
    'Referer': 'http://172.16.6.107:7001/swagger-ui.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,tr;q=0.7',
}

data = '{ "loginName": "yefan@vv.cn", "organizeType": 4, "password": "Admin123"}'

response = requests.post('http://172.16.6.107:7001/api/user/v1/account/login', headers=headers, data=data, verify=False)
print(response.text)

# -*- coding: utf-8 -*-

import json
import httplib

hdr = {"content-type": "application/json"}

conn = httplib.HTTPConnection('my-url')
conn.request('POST', '/api/Html', json.dumps(payload), hdr)
response = conn.getresponse()
data = response.read() # same as r.text in 3.x

# -*- coding: utf-8 -*-
from urllib import urlencode
import urllib2

def http_post(url, data):
    post = urlencode(data)
    req = urllib2.Request(url, post)
    response = urllib2.urlopen(req)
    return response.read()

data={"loginName":"yefan@vv.cn","organizeType":"4","password":"Admin123"}
url = '127.0.0.1:7001/api/user/v1/account/register'
rs = http_post(url, data)
print rs

import urllib
import urllib2

url = 'http://127.0.0.1:7001/api/user/v1/account/register'
values = {'loginName' : 'yefan@vv.cn',
          'organizeType' : '4',
          'password' : 'Admin123' }

data = urllib.urlencode(values)
try: urllib2.Request(url, data)
except urllib2.URLError as e:
    print e.reason
the_page = response.read()
print the_page

curl - d "loginName=yefan@vv.cn&password=Admin123?organizeType=4" "http://127.0.0.1:7001/api/user/v1/account/login"

7001/api/user/v1/account/login

{

    "loginName": "yefan@vv.cn",

    "organizeType": 4,
    "password": "Admin123"

}

{"loginName": "yefan@vv.cn", "organizeType": 4, "password": "Admin123"}

curl -i -k  -H "Content-type: application/json" -X POST -d '{"loginName": "yefan@vv.cn", "organizeType": 4, "password": "Admin123"}' http://127.0.0.1:7001/api/user/v1/account/login

curl -i -k  -H "Content-type: application/json" -X POST -d '{"loginName":"yefan@vv.cn","organizeType":"4","password":"Admin123"}' http://127.0.0.1:7001/api/user/v1/account/register

http://172.16.6.129:8001/api/bd/mdc/v1/registerMerchant?ocrMerchantId=12


curl -d "ocrMerchantId=12" "http://127.0.0.1:8001/api/bd/mdc/v1/registerMerchant?ocrMerchantId=12"
curl "http://127.0.0.1:8001/api/bd/mdc/v1/registerMerchant?ocrMerchantId=12"


import urllib
import urllib2
import json


url = 'http://127.0.0.1:7001/api/user/v1/account/login'
values = {'loginName':'yefan@vv.cn','organizeType':'4','password':'Admin123'}
data = data = json.dumps(values)
response = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(response)
print f.info()
response = f.read()
print response


url = 'http://www.someserver.com/cgi-bin/register.cgi'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}

data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read()

