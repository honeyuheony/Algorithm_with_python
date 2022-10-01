'''
programmers level2 숫자의 표현
https://school.programmers.co.kr/learn/courses/30/lessons/12924
'''


def solution(n):
    part_sum = [0, 1]
    for i in range(2, n+1):
        part_sum.append(part_sum[i-1] + i)
    start, end = 0, 1
    answer = 0
    while start != end:
        temp = part_sum[end] - part_sum[start]
        if temp > n:
            start += 1
            continue
        if temp == n:
            answer += 1
            start += 1
        if end < n:
            end += 1
    return answer


print(solution(15))
