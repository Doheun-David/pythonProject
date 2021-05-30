import os
import sys
import urllib.request
import json
import re

검색어 = input("책검색 : ")
client_id = "ke00X3ErXW7Rf2Bt44vH"
client_secret = "fJ25ZPcCS4"
encText = urllib.parse.quote("검색할 단어")
url = "https://openapi.naver.com/v1/search/book.json?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    검색결과 = response_body.decode('utf-8')

    json결과 = json.loads(검색결과)

    for i in json결과['items']:
        타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
        print( 타이틀 )
else:
    print("Error Code:" + rescode)



