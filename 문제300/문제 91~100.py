
# 문제 91
아이스크림 = {"메로나" : [300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
# 문제 92
아이스크림 = {"메로나" : [300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
print("메로나의 가격 : ",아이스크림["메로나["0]])
# 문재 93
아이스크림 = {"메로나" : [300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
print("메로나의 제고 : ",아이스크림["메로나"[1]])
# 문제 94
아이스크림 = {"메로나":[300,20],
             "비비빅":[400,3],
             "죠스바":[250,100]}
아이스크림["월드콘"] = [500, 7]
print(아이스크림)

# 문제 95
아이스크림 = {"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
아이스크림이름 = list(아이스크림.keys())
print(아이스크림)
# 문제 96
아이스크림 = {"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
아이스크림가격 = list(아이스크림.values())
print(아이스크림가격)

# 문제 97
아이스크림 = {"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
print("아이스크림의 총 합계 : ", sum(아이스크림.values()))
# 문제 98
아이스크림 = {"탱크보이":1200, "폴라포":1200, "빵빠레":1800, "월드콘":1500, "메로나":1000}
새로운아이스크림 = {"팥빙수":2700, "아맛나":1000}

아이스크림.update(새로운아이스크림)
print(아이스크림)
# 문제 99
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
딕셔너리 = dict(zip(keys, vals))
print(딕셔너리)
# 문제 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10000, 11000]
딕셔너리 = dict(zip(date, close_price))
print(딕셔너리)