# programmers level1 폰켓몬
# https://programmers.co.kr/learn/courses/30/lessons/1845
import itertools


def solution(nums):
    answer = len(nums) // 2 if len(set(nums)
                                   ) >= len(nums) // 2 else len(set(nums))
    return answer
