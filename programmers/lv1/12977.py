# programmers level1 소수만들기
# https://programmers.co.kr/learn/courses/30/lessons/12977
# 순열과 조합 사용 모듈
import itertools


def solution(nums):
    combination = list(itertools.combinations(nums, 3))
    answer = 0
    for c in combination:
        c = sum(c)
        for n in range(2, c):
            if c % n == 0:
                break
            elif n == c - 1:
                answer += 1
    return answer


nums = [1, 2, 7, 6, 4]
print(solution(nums))
