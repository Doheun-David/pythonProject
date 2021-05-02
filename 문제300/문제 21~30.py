# 문제 21 : 인덱싱[문자순서] : 0번시작
letters = 'python'
print( letters[0] , letters[2] )

# 문제 22 : 슬라이싱[시작번호, 끝번호, 단위]
    #시작번호부터 끝번호 전까지 문자 출력
license_plate="24가 2210"
print(license_plate[4:8])

# 문제 23
string = "홀짝홀짝홀짝"
print(string[0:6:2]) # 0부터 6전까지 2씩 증가
# 문제 24
string = "PYTHON"
print(string[ : : -1]) # 뒤에서부터 시작
# 문제 25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
# 문제 26
phone_number2 = phone_number1.replace(" ", "")
print(phone_number2)

# 문제 27
url = "http://sharebook.kr"
print(url[17:19])

# 문제 28
lang = 'python'
lang[0] = 'P'
print(lang)
# 문제 29
string = "abcdfe2a354a32a"
string1 = string.replace("a", "A")
print(string1)

# 문제 30 예상 : 소문자 b가 대문자 B로 바뀔것으로 예상된다.
string0 = 'abcd'
string0.replace('b', 'B')
print(string)