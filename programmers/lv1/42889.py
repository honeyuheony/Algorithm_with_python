# programmers level1 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
import math


def solution(N, stages):
    arrive_count = [0 for _ in range(N)]
    fail_count = [0 for _ in range(N)]
    for stage in stages:
        for i in range(stage-1):
            arrive_count[i] += 1
        if stage <= N:
            arrive_count[stage-1] += 1
            fail_count[stage-1] += 1
    answer = [fail_count[n] / arrive_count[n]
              if arrive_count[n] != 0 else 0 for n in range(N)]
    temp = []
    for i in sorted(answer, reverse=True):
        temp.append(answer.index(i)+1)
        answer[answer.index(i)] = -1
    answer = temp
    return answer


# Test
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))
