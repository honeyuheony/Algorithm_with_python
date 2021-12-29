# programmers level1 정수 제곱근 판별
# https://programmers.co.kr/learn/courses/30/lessons/12934
import math


def solution(n):
    return math.pow(math.sqrt(n)+1, 2) if math.isqrt(n) == math.sqrt(n) else -1


print(solution(10))
