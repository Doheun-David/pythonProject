
# 문제 9
def solution(characters):
    result = ""
    for i in range(len(characters)):
        if characters[i-1] != characters[i]:
            result += characters[i]

    return result

characters = "sentencccccceeeeeee"
ret = solution(characters)
print("solution 함수 결과", ret)