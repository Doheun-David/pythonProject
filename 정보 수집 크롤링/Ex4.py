
# 자동차 모델명 입력을 받아 출시가 크롤링
from bs4 import BeautifulSoup as bs
import urllib.request as ur
import urllib

while True : # 계속 입력받기
    모델명 = input("모델명 : ")
    검색어 = urllib.parse.quote(모델명)
    주소 = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9E%90%EB%8F%99%EC%B0%A8+%EB%AA%A8%EB%8D%B8&oquery=%ED%98%84%EC%9E%AC+%EB%AA%A8%EB%8D%B8&tqi=h7cWgsp0J1ZssMA8LkossssssQG-361267"

    웹문서 = ur.urlopen(주소)
    soup = bs(웹문서.read(), 'html.parser')
    가격 = soup.find_all("span", {"class":""})
    찾는문자 = "판매"
    for i in 가격:
        b = 찾는문자 in i.text
        if b:
            print("현재 모델의 출시가 : "+ i.text)

# 무한 입력받기
