# 문제 51번
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 문제 52번 : 리스트명.append(추가할 변수) : 리스트에 변수 추가
movie_rank.append("배트맨")

# 문제 53번 : 리스트명.insert(인덱스 번호, 추가할 변수) : 인덱스 위치에 추가
movie_rank.insert(1, "슈퍼맨") #1번 인덱스에 슈퍼맨 추가

# 문제 54번 : del
del movie_rank[3] # 럭키 삭제

# 문제 55번
del movie_rank[2] #스플릿 삭제 => 배트맨 => 스플릿 자리로 이동
del movie_rank[2]

# 문제 56번 : 리스트 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
리스트 = lang1 + lang2
print(리스트)

# 문제 57번
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

# 문제 58번
num = [1, 2, 3, 4, 5]
print(sum(num))

# 문제 59번
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))
# 문제 60번
num1 = [1, 2, 3, 4, 5]
평균 = sum(num1) / len(num1)
print(평균)