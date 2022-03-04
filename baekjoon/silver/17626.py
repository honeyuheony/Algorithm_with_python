# baekjoon s4 Four Squares
# https://www.acmicpc.net/problem/17626

import sys
import math
input = sys.stdin.readline
n = int(input())

dp = [0, 1]
for i in range(2, n+1):
    minvalue = math.inf
    j = 1
    while (j**2) <= i:
        minvalue = min(minvalue, dp[i - (j**2)])
        j += 1
    dp.append(minvalue+1)
print(dp[n])
