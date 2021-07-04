# 문제 51번
movie_rank = ["닥터스트레인지", "스플릿", "럭키"]

# 문제 52번
movie_rank.append("배트맨")

# 문제 53번
movie_rank.insert(1, "슈퍼맨")

# 문제 54번
movie_rank.remove("럭키")

# 문제 55번
movie_rank.remove("스플릿")
movie_rank.remove("배트맨")

# 문제 56번
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2

# 문제 57번
nums = [1, 2, 3, 4, 5, 6, 7]
print("max : ",max(nums))
print("min : ",min(nums))

# 문제 58번
nums = [1, 2, 3, 4, 5]
a = 0
for i in range(len(nums)):
    a += nums[i]
print(a)

# 문제 59번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 문제 60번
nums = [1, 2, 3, 4, 5]
u = 0
for i in range(len(nums)):
    u += nums[i]
print(u/len(nums))

# 문제 61번
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1 : ])

# 문제 62번
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0 : : 2])

# 문제 63번
print(nums[1 : :2])

# 문제 64번
nums = [1, 2, 3, 4, 5]
print(nums[ : :-1])

# 문제 65번
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 문제 66번
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[0], interest[1], interest[2], interest[3], interest[4])

# 문제 67번
print(interest[0],"/",interest[1],"/",interest[2],"/",interest[3],"/",interest[4])

# 문제 68번
print(interest[0],"\n",interest[1],"\n",interest[2],"\n",interest[3],"\n",interest[4])

# 문제 69번
string = "삼성전자/LG전자/Naver"
print(string.split("/"))

# 문제 70번
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# 문제 71번
my_variable = ( )

# 문제 72번
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 문제 73번
튜플 = (1)

# 문제 74번
t = (1, 2, 3, 4)

# 문제 75번
t = 1, 2, 3, 4

# 문제 76번
e = ('a', 'b', 'c')

# 문제 77번
interest = ('삼성전자', 'LG전자', 'SK Hynix')

# 문제 78번
interest = ['삼성전자', 'LG전자', 'SK Hynix']

# 문제 79번
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 문제 80번

# 문제 81번
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
valid_score = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5]

# 문제 82번
valid_scores = [9.4, 7.8, 9.5, 9.9, 9.7, 9.3, 9.2, 8.7]

# 문제 83번
valid__score = [8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8]

# 문제 84번
temp = [ ]

# 문제 85번
ui = {"메로나":1000,"폴라포":1200, "빵빠레":1800}

# 문제 86번
ui["죠스바"] = 1200
ui["월드콘"] = 1500

# 문제 87번
print("메로나 가격 :", ui["메로나"])

# 문제 88번
ui["메로나"] = 1300

# 문제 89번
del ui["메로나"]

# 문제 90번
# 딕셔너리에 누가바가 없어서

# 문제 91번
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

# 문제 92번
print(inventory["메로나"][0])

# 문제 93번
print(inventory["메로나"][1])

# 문제 94번
inventory["월드콘"] = [500, 7]

# 문제 95번
icecream = {"탱크보이": 1200, "폴라포": 1200, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}
print(list(icecream.keys()))

# 문제 96번
print(list(icecream.values()))

# 문제 97번
print(sum(list(icecream.values)))

# 문제 98번
new_product = {"팥빙수":2700, "아맛나":1000}
print(inventory.update(new_product))

# 문제 99번

# 문제 100번
data = ["09/05", "09/06", "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]

# 문제 101번
# 참, 거짓

# 문제 102번
print(3 == 5)

# 문제 103번
print(3<5)

# 문제 104번
x = 4
print(1<x<5)

# 문제 105번
print((3==3)and(4!=3))

# 문제 106번
# 부호가 잘못되었다

# 문제 107번
if 4<3:
    print("Hello World")

# 문제 108번
if 4<3:
    print("Hello World")
else:
    print("Hi there")

# 문제 109번
if True :
    print("1")
    print("2")
else:
    print("3")
print("4")

# 문제 110번
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5")

# 문제 111번
sfs = input()
print(sfs*2)

# 문제 112번
drf = input("하나의 숫자 입력 : ")
print(drf+10)

# 문제 113번
wrwr = input("하나의 숫자 입력 : ")
if wrwr%2==0:
    print("짝수")
else:
    print("홀수")

# 문제 114번
wtwt = input("하나의 숫자 입력 : ")
if wtwt+20<=255:
    print(wtwt+20)
elif wtwt+20>255:
    print(255)

# 문제 115번
fd = input("하나의 숫자 입력 : ")
if fd-20<0:
    print(0)
elif fd-20>=0:
    print(fd-20)
elif fd-20>255:
    print(255)

# 문제 116번
yy = input("현재 시간 입력(분단위로) : ")
if yy%60==0:
    print("정각입니다")
else:
    print("정각이 아닙니다")

# 문제 117번
ooo = 0
fruit = ["사과", "포도", "홍시"]
uuu = input("좋아하는 과일은? ")
for i in range(len(fruit)):
    if uuu == fruit[i-1]:
        ooo+=1
    else:
        ooo-=1
if ooo == -1:
    print("정답입니다")
elif ooo == -3:
    print("오답입니다")

# 문제 118번
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
iiii = 0
pp = input("투자 경고 종목 입력 : ")
for i in range(len(warn_investment_list)):
    if pp == warn_investment_list[i-1]:
        iiii+=1
    else:
        iiii-=1
if iiii == -1:
    print("투자 경고 종목입니다")
elif iiii == -3:
    print("투자 경고 종목이 아닙니다")

# 문제 119번
날씨 = {"봄":"딸기", "여름":"토마토", "가을":"사과"}

# 문제 120번

# 문제 121번
vvv = input("문자 한개 입력 : ")
if islower(vvv):
    print(upper(vvv))
else:
    print(lower(vvv))

# 문제 122번
