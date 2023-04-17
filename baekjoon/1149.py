# baekjoon s1 rgb거리
# https://www.acmicpc.net/problem/1149

import sys
input = sys.stdin.readline

N = int(input())
house = [[0, 0, 0]]
dp = [[0, 0, 0] for i in range(N+1)]
for _ in range(N):
    house.append(list(map(int, input().split())))
dp[1] = house[1]
for i in range(2, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i][2]
print(min(dp[N]))
