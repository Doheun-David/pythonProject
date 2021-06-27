def solution(price, money):
    answer = money-sum(price)
    if answer <0:
        answer = -1
    return answer