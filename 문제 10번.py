def solution(arr, k):
    answer = 0
    lst = []
    n = len(arr)

    for i in range(n):
        for j in range(4):
            lst.append(arr[i][j])

    lst.sort()
    answer = lst[k - 1]
    return answer