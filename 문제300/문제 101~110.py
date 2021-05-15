
    #논리 : 맞는지 틀린지 판단
    #연산자 :
        #산출연산자 : + 더하기 - 빼기 * 곱하기 / 나누기 //나누기[몫] % 나누기[나머지]
        #비교연산자 : > 초과 < 미만 >= 이상 <=이하 == 같다 !=같지 않다
        #논리연산자 : and[이면서] or [이거나] ![부정]
        #대입연산자 : +=[오른쪽 값을 왼쪽값에 더하기 후 왼쪽값에 대입]
            #       -=[오른쪽 값을 왼쪽값에 빼기 후 왼쪽값에 대입
            #   *= /=
    #IF : 논리문
    #       if 논리 :
    #           참[코드]
    #       else:
    #           거짓[코드]

# 문제 101
print(type(True))
print(type(False))
# 문제 102
print(3==5)
# 문제 103
print(3<5)
# 문제 104
x = 4
print(1<x<5)
# 문제 105
print((3==3) and (4!=3))
# 문제 106
False
print("=>라는 연산자는 없다")
# 문제 107
if 4<3:
    print("Hello World")
# 문제 108
if 4<3:
    print("Hello World")
else:
    print("Hi, there")
# 문제 109
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")
# 문제 110
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")