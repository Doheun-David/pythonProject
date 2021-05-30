
# 네이버 검색 API 이용한 JSON 가공 프로그램
    # JSON : 키-값 => 한쌍 <--- 딕셔너리와 유사

import urllib.request
import json
import re

def 네이버검색(카테고리, 검색결과수):
    client_id = "ke00X3ErXW7Rf2Bt44vH"
    cliend_secret = "fJ25ZPcCS4"
    url = "https://openapi.naver.com/v1/search/" + 카테고리 + ".json"
    option = "&display=" + 검색결과수 + "&sort = count" # display : 출력 갯수 : 검색결과 수
    query = "?query="+urllib.parse.quote(input(카테고리+"검색 정보 입력 : "))
    url_query = url+query+option

    검색어 = input("책검색 : ")
    client_id = "ke00X3ErXW7Rf2Bt44vH"
    client_secret = "fJ25ZPcCS4"
    encText = urllib.parse.quote("검색할 단어")
    url = "https://openapi.naver.com/v1/search/book.json?query=" + encText  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        검색결과 = response_body.decode('utf-8')

        json결과 = json.loads(검색결과)

        for i in json결과['items']:
            타이틀 = re.sub('<.+?>', '', i['title'], 0, re.I | re.S)
            print("--->검색결과 : " + 타이틀)

            if 카테고리 == "shop":
                print("--->최적가 : ", i['lprice'])
            if 카테고리 == "movie":
                print("---> 평점 : ", i['userRating'])
            if 카테고리 == "news":
                print("---> 주요내용 : ", i[])


    else:
        print("Error Code:" + rescode)


while True:
    print("검색[naverAPI] 프로그램")
    print("카테고리[1.뉴스 2.쇼핑 3.도서] 0.종료")
    선택 = int(input("선택 : ")) # 입력받아 선택변수에 저장
    # 선택 제어
    if 선택 == 1:
        카테고리 = "news"
        검색결과수 = input("--->뉴스를 선택했습니다. 몇개 출력핡까요?")
        네이버검색(카테고리, 검색결과수) # 함수 불러내기
    if 선택 == 2:
        카테고리 = "shop"
        검색결과수 = input("--->쇼핑 선택했습니다. 몇개 출력핡까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 3:
        카테고리 = "book"
        검색결과수 = input("--->책 선택했습니다. 몇개 출력핡까요?")
        네이버검색(카테고리, 검색결과수)
    if 선택 == 0:
        print("---> 이용해주셔서 감사합니다")
        break