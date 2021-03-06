#-*- coding: utf-8 -*-
import os
import sys
import json
import re

import urllib.request
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
url = "https://openapi.naver.com/v1/datalab/search";
body = "{\"startDate\":\"2017-01-01\",\"endDate\":\"2017-04-30\",\"timeUnit\":\"month\",\"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},{\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\"device\":\"pc\",\"ages\":[\"1\",\"2\"],\"gender\":\"f\"}";

body = {
        "startDate":"2019-05-30",
        "endDate":"2021-05-30",
        "timeUnit":"date",
        "category":[{"name":"면세점", "param":["500000010"]}],
        "device":"",
        "gender":"",
        "ages":[ ]
}
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

검색결과 = response_body.decade('utf-8')
json결과 = json.loads(검색결과)

for i in json결과['result']:
    데이터 = i['data']
    print(데이터)

print(데이터[0]['ratio']) # 클릭 수