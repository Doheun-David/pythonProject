
# 크롤링 : 인터넷에서 데이터 추출하기

from bs4 import BeautifulSoup as bs
import urllib.request as ur

url = 'http://quotes.toscrape.com/' # 인터넷 주소 넣기
html = ur.urlopen(url) # 인터넷을 파이썬에서 열기해서 html 변수에 저장

soup = bs(html.read(), 'html.parser') #read() : 인터넷을 읽어오기

print(soup.find_all('span')[0].text) #읽어온 파일 중 찾기('span') 찾아서 첫번째 택스트 가져오기
# 마크업 언어[html] 예시 <spans> 태그를 찾아서 태그 사이에 있는 택스트 가져오기

# find_all() : 찾는 값 모두 가져오기
print(soup.find_all('span')[2].text)

print(soup.find_all('span')[4].text)

for i in soup.find_all('span'):
    print(i.text)

# span 에 포함된 클래스만 찾기
for i in soup.find_all("div", {"class":"quote"}):
    print(i.text)