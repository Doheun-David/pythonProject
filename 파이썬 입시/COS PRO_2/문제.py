
# 문제 1 : 리스트에 저장된 문자열의 갯수를 다시 리스트에 담기

def solution(shirt_size) : # 함수 만들기
    # 지문 보고 문제 풀기~~~
    size_count = [0, 0, 0, 0, 0, 0]

    for ss in shirt_size : # 리스트 반복 => 리스트내 항목이 변수에 하나씩 대입
        if ss == "XS":
            size_count[0] += 1
        if ss == "S":
            size_count[1] +=1
        if ss == "M":
            size_count[2] +=1
        if ss == "L":
            size_count[3] +=1
        if ss == "XL":
            size_count[4] +=1
        if ss == "XXL":
            size_count[5] +=1
    return size_count
    answer = [ ] # 리스트
    return answer # 함수가 끝나면서 돌려주는 값 => return => 리스트를 리턴

shirt_size = ["XS", "S","M", "L", "XL", "S"]
ret = solution(shirt_size) # 함수 불러내기

print("solution : return value of the function", ret, " .")

# 문제 2

def solution(price, grade):
    answer = 0

    if grade == "S":
        answer = price*0.95
    if grade == "G":
        answer = price*0.9
    if grade == "V":
        answer = price * 0.85

    return int(answer)

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

print("Solution: return value of the function in", ret1, ".")

price2 = 96900
grade2 = "0"
ret2 = solution(price2, grade2)

print("Solution: return value of the function in", ret2, ".")

# 문제 3

def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 13, 31, 30, 31, 30, 31]
    total = 0;
    for i in range(month-1):
        total += month_list[i]
    total += day
    return total -1

def solution(start_month, start_day, end_month, end_day):
    start_total = func_a(start_month, start_day)
    end_total = func_a(end_month, end_day)
    return end_total - start_total

start_month = 1
start_day = 2
end_month = 2
end_day = 2
ret = solution(start_month, start_day, end_month, end_day)

print("Solution: return value of the function is", ret, ".")

# 문제 4

def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
        return ret

def func_c(arr):
    INF = 1001
    ret = INF
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):
    counter =func_c(arr)
    max_cnt = func_b(counter)
    min_cnt = func_c(counter)
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print("Solution : return value of the function is", ret, ".")

# 문제 5
def solution(arr):
    left, right = 0, len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right-= 1
    return arr

    # left가 0일 경우 right도 0 => 반복문 실행
        # arr[0], arr[0] = arr[0], arr[0]
            #1      #1      #1      #1
        #left + 1       right-1
        #left 1일경우 right -1
        #arr[1], arr[-1] = arr[-1], arr[1]
            #4      #3      #3      #4
        # left +1 right-1
        # left 2일경우 right -2
            # arr[2], arr[-2] = arr[-2], arr[2]
arr = [1, 4, 2, 3]
ret = solution(arr)

print("Solution: return value of the function is", ret, ".")

# 문제 6
def solution(number):
    count = 0
    for i in range(1, number+1):
        current = i
        temp = count
        while current != 0:
            if current %10 == 3 or current %10 == 6 or current % 10 == 9:
                count += 1
                print("pair", end = '')
            current = current // 10
        if temp == count:
            print(i, end = '')
        print(" ", end = '')
    print("")
    return count