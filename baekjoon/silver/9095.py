# baekjoon s3 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
# DP, 점화식

import sys
input = sys.stdin.readline

dp = [1, 2, 4]
T = int(input())
for _ in range(T):
    n = int(input())
    if n > len(dp):
        for i in range(len(dp)-1, n+1):
            dp.append(dp[i] + dp[i-1] + dp[i-2])

    sys.stdout.write(str(dp[n-1])+'\n')
