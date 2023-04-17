# baekjoon s5 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

N = int(input())
point = []
for _ in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

point.sort(key=lambda x: (x[0], x[1]))

for p in point:
    print(p[0], p[1])
