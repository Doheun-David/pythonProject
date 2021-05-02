#문제 31번 예상 : 문자끼리는 더할 수 없고 연결된다.
a = "3"
b = "4"
print(a + b)

# 문제 32번
print("Hi" * 3)

# 문제 33번
print("-" * 80)

# 문제 34번
t1 = 'python'
t2 = 'java'
print((t1 + t2) * 4)

# 문제 35번
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 : %s 나이 : %d " % (name1, age1))
print("이름 : %s 나이 : %d " % (name2, age2))

# 문제 36번 format() 함수 : () 안에 들어갈 데이터를 format 함수 안에 넣기

print("이름 : {} 나이 : {}", format(name1, age1))
print("이름 : {} 나이 : {}", format(name2, age2))


# 문제 37번 f-string

print( f"이름 : {name1} 나이 : {age1}")
print( f"이름 : {name1} 나이 : {age1}")
# 문제 38번
상장주식수 = "5,969,782,550"
상장주식수1 = 상장주식수.replace(",", "")
print(상장주식수1)

#문제 39번
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])

#문제 40번 공백제거 strip() 함수 사용시 앞뒤에 공백 제거 함수
data = "        삼성전자        "
공백제거 = data.strip()
print(공백제거)