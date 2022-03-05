# baekjoon s1 정수삼각형
# https://www.acmicpc.net/problem/1932

import sys
input = sys.stdin.readline

tree = []
dp = []
N = int(input())
for _ in range(N):
    tree.append(list(map(int, input().split())))
dp.append(tree[0])
for i in range(1, N):
    temp = []
    for index, t in enumerate(tree[i]):
        max_value = 0
        if index > 0:
            max_value = max(max_value, dp[i-1][index-1] + t)
        if index < len(tree[i])-1:
            max_value = max(max_value, dp[i-1][index] + t)
        temp.append(max_value)
    dp.append(temp)
print(max(dp[N-1]))
