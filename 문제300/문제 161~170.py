
# 문제 161
for 변수 in range(100):
    print(변수)

# 문제 162
for 변수 in range(2002, 2051, 4):
    print(변수)

# 문제 163
for 변수 in range(3, 31, 3):
    print(변수)

# 문제 164
for 변수 in range(99, -1, -1):
    print(변수)
# 문제 165
for 변수 in range(10):
    print(변수/10)
# 문제 166
for 곱 in range(1, 10):
    print(3, "X", 곱, "=", 3*곱)
# 문제 167
for 곱 in range(1, 10):
    if 곱%2==1:
        print(3, "X", 곱, "=", 3*곱)
# 문제 168
합계 = 0
for 변수 in range(1, 11):
    합계 += 변수

print("누적합계 : ", 합계)
# 문제 169
합계 = 0
for 변수 in range(1, 11):
    if 변수%2==1:
        합계 += 변수
print("홀수 누적합계 : ", 합계)

# 문제 170
누적곱 = 1
for 변수 in range(1, 11):
    누적곱 += 변수

print("누적곱 : ", 누적곱)