# 문제 41번 : upper() 함수 : 대문자로 변환 해주는 함수
ticker = "btc_krw"
print(ticker.upper())

# 문제 42번 : lower() 함수 : 소문자로 변환해주는 함수
ticker1 = "BTC_KRW"
print(ticker1.lower())

# 문제 43번 : capitalize() 함수 : 첫글자만 대문자로 변환해주는 함수
ticker2 = "btn_krw"
print(ticker2.capitalize())

# 문제 44번 : endswith() 함수 : 끝나는 문자가 맞는지 확인 함수
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 문제 45번
print(file_name.endswith("xlsx"))

# 문제 46번
file_name1 = "2020_보고서.xlsx"
print(file_name1.startswith("2020"))

# 문제 47번
a = "hello world"
print(a.split())
# 문제 48번
ticker = "btc_krw"
print(ticker.split("_"))

#문제 49번
date = "2020-05-01"
print(date.split("-"))

# 문제 50번
date = "  039490  "
print(date.rsplit())