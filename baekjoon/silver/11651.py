# baekjoon s5 좌표정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline

N = int(input())
point = []
for _ in range(N):
    a, b = map(int, input().split())
    point.append((a, b))
point.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(point[i][0], point[i][1])
