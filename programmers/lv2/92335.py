'''
programmers level2 k진수에서 소수 개수 구하기
https://programmers.co.kr/learn/courses/30/lessons/92335
'''
import math


def decimal_to_k(num: int, k: int) -> str:
    k_num = ''
    while num:
        num, mod = divmod(num, k)
        k_num += str(mod)

    return k_num[::-1]


def is_prime(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def check_condition(k_num, start, end):
    p = k_num[start:end]
    if (start == 0 or k_num[start-1] == '0') \
            and \
            (end == len(k_num) or k_num[end] == '0') \
            and \
            not '0' in p:
        return True
    else:
        return False


def solution(n, k):
    answer = 0
    k_num: str = decimal_to_k(n, k)
    start, end = 0, 0
    while end < len(k_num):
        end += 1
        if is_prime(int(k_num[start:end]))\
                and check_condition(k_num, start, end):
            start = end
            answer += 1
        elif k_num[end-1] == '0':
            start = end

    return answer


print(solution(437674, 3))
