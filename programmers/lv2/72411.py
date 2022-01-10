# programmers level2 메뉴 리뉴얼
# https://programmers.co.kr/learn/courses/30/lessons/72411
# 조합
# 1. n개로 이루어진 음식조합 목록 구하기 combination
# 2. 가장 많은 음식조합만 저장
# collections.counter 기억하기

import itertools


def solution(orders, course):
    recode = []
    answer = []
    for c in reversed(course):
        for o in orders:
            o = ''.join(sorted(o))
            recode += map(lambda x: ''.join(x),
                          list(itertools.combinations(o, c)))
        recode_dict = {}
        while(len(recode)):
            r = recode.pop(0)
            try:
                recode_dict[r] += 1
            except:
                recode_dict[r] = 1
        answer += [key for key, value in recode_dict.items() if value ==
                   max(recode_dict.values()) and value > 1]
    return sorted(answer)


# Test Code
print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
