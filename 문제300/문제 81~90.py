#딕셔너리{}
    # 하나의 키와 값으로 이루어진 한 쌍을 여러개 저장
    # 딕셔너리 명 = {키 : 값, 키2:값2, 키3:값3)
# 문제 81
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
print(*scores) # 리스트 제거
scores,_,_ = scores # 뒤에서 2개 생략
print(scores)

# 문제 82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,_,*scores = scores # 앞에서 2개 생략
print(scores)
# 문제 83
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_,*scores,_ = scores # 앞뒤로 1개씩 생략
# 문제 84
temp = { }

# 문제 85
아이스크림 = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}

# 문제 86
아이스크림 = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
아이스크림["죠스바"] = 1200
아이스크림["월드콘"] = 1500

# 문제 87
아이스크림 = {"베로나":1000,
    "폴라포":1200,
    "빵빠레":1800,
    "죠스바":1200,
    "월드콘":1500}
print("메로나 가격 : ", 아이스크림["메로나"])
# 문제 88
아이스크림 = {"베로나":1000,
    "폴라포":1200,
    "빵빠레":1800,
    "죠스바":1200,
    "월드콘":1500}
아이스크림["메로나"] = 1300
print("메로나 가격 : ", 아이스크림["메로나"])
# 문제 89
아이스크림 = {"베로나":1000,
    "폴라포":1200,
    "빵빠레":1800,
    "죠스바":1200,
    "월드콘":1500}
del 아이스크림["메로나"] # del : 삭제
print(아이스크림)