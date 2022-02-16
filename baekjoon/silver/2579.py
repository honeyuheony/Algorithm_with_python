# baekjoon s3 계단오르기
# https://www.acmicpc.net/problem/2579
# 다이나믹프로그래밍
# 답보고품

import sys
input = sys.stdin.readline

stairs = [0]
N = int(input())
for _ in range(N):
    stairs.append(int(input()))

if N < 3:
    print(sum(stairs))
else:
    dp = [0 for i in range(N+1)]
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    dp[3] = max(stairs[1], stairs[2]) + stairs[3]
    for i in range(4, N+1):
        dp[i] = max((dp[i-3] + stairs[i-1]), dp[i-2]) + stairs[i]
    print(dp[N])
