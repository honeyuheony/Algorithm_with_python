# baekjoon s3 파도반 수열
# https://www.acmicpc.net/problem/9461
# 다이나믹프로그래밍, 수학

import sys
input = sys.stdin.readline

p = [0, 1, 1, 1, 2, 2]
T = int(input())
for _ in range(T):
    n = int(input())
    if n <= len(p)-1:
        print(p[n])
    else:
        for i in range(len(p), n+1):
            p.append(p[i-1] + p[i-5])
        print(p[n])
