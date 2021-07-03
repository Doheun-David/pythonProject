# 문제 51번
movie_rank = ["닥터스트레인지", "스플릿", "럭키"]

# 문제 52번
movie_rank.append("배트맨")

# 문제 53번
movie_rank.append("슈퍼맨")

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
e[0] = 'A'
# 문제 77번
interest = ('삼성전자', 'LG전자', 'SK Hynix')

# 문제 78번
interest = ['삼성전자', 'LG전자', 'SK Hynix']