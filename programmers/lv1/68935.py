# programmers level1 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

import math


def solution(n):
    answer = 0
    reverse = []
    p = math.floor(math.log(n, 3))
    for i in range(p, -1, -1):
        div = n // pow(3, i)
        n -= div * pow(3, i)
        reverse.append(div)
    for index, i in enumerate(reverse):
        answer += i * pow(3, index)
    return answer


print(solution(45))
