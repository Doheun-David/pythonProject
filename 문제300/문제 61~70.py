# 데이터를 저장하는 방법 4가지의 차이와 사용방법
    # 변수 =
    # 리스트 =
    # 튜플 =
    #딕셔너리 =

# 문제 61 # price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])
    #[인덱싱] = [1:] = 2번째 값부터 끝까지

# 문제 62 # 슬라이싱을 사용해서 홀수만 출력하라
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[ : :2])
    #[인덱싱] = [ : : 2] = 0번째 값부터 끝까지 2개씩 이동]
    #[ 시작번호 : 끝번호 : 이동단위 ]

# 문제 63
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(num[1 : :2])
    #[인덱싱] = [1 : : 2] = 1번째 값부터 끝까지 2개씩 이동 =

# 문제 64
nu = [1, 2, 3, 4, 5]
print(nu[ : : -1])
    #[슬라이싱] = [ : : 1] = 뒤로 이동

# 문제 65
interest = ['삼성전자', 'LG전자', 'NAVER']
print(interest[0], interest[2])

# 문제 66
interests = ['삼성전자', 'LG전자', 'NAVER', 'SK하이닉스', '미래에셋대우']
print(" ".join(interests))
    # join 함수 : 리스트 내 항목을 합칠 때 사용
    # 항목들 사이에 ""안에 들어간걸 추가한다.

# 문제 67
interests = ['삼성전자', 'LG전자', 'NAVER', 'SK하이닉스', '미래에셋대우']
print("/".join(interests))

# 문제 68
interests = ['삼성전자', 'LG전자', 'NAVER', 'SK하이닉스', '미래에셋대우']
print("\n".join(interests))
    #\n : 줄바꿈 제어 문자      \t : 들여쓰기 제어 문자

# 문제 69
string = "삼성전자/LG전자/NAVER"
interest = string.split("/")
print(interest)


# 문제 70
    #오름차순
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
    #내림차순
data.sort(reverse = True)
print(data)