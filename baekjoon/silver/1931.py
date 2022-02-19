# baekjoon s2 회의실배정
# https://www.acmicpc.net/problem/1931
# 그리디
# 1. 끝나는 시간 1순위, 시작하는 시간 2순위로 정렬
# 2. 순차탐색으로 하나씩 시간표에 넣을 수 있는지 검사 후 넣기

import sys
input = sys.stdin.readline

T = int(input())
table = []
for _ in range(T):
    a, b = map(int, input().split())
    table.append((a, b))
table.sort(key=lambda x: (x[1], x[0]))
result = []
for t in table:
    if not len(result) or result[len(result)-1][1] <= t[0]:
        result.append(t)
print(len(result))
