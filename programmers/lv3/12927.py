'''
programmers level3 야근 지수
https://programmers.co.kr/learn/courses/30/lessons/12927
'''
from collections import Counter


def solution(n, works):
    works = {key: value for key, value in Counter(works).most_common()}
    for i in range(max(works.keys()), 0, -1):
        if n >= works[i]:
            n -= works[i]
            works.setdefault(i-1, 0)
            works[i-1] += works[i]
            works[i] = 0
        else:
            mod = n % works[i]
            works.setdefault(i - 1, 0)
            if mod != 0:
                works[i] -= mod
                works[i-1] += mod
            return sum([value * (key**2) for key, value in works.items()])





