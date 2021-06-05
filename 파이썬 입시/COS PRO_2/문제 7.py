
# 문제 7

def solution(scores):
    count = 0
    for s in scores: # 토익 시험 특정 조선을 충족하면 초급영어강의 수강 대상 구하기
        if 650 <= s or s < 800: # 토익시험 650 이상 800 미만
            count+1
    return count

scores = [650, 722, 714, 558, 714, 803, 650, 679, 669, 800] # 수강신청한 사람들의 토익 점수
ret = solution(scores)

print("solution 함수 결과 : ", ret, ".")