# programmers level1 두개뽑아서더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644
# 두 수 뽑아 더하기 -> combination

import itertools


def solution(numbers):
    answer = [sum(i) for i in itertools.combinations(numbers, 2)]
    answer = answer.sort()
    return answer
