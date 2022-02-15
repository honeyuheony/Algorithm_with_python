# baekjoon s3 1로만들기
# https://www.acmicpc.net/problem/1463
# 다이나믹 프로그래밍
# 1. 1 ~ n 까지 수에 대해 각각 그 수까지 가는데에 소요되는 연산횟수를 기록한다.
# 답보고풀었음
import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2]+1

    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1

print(dp[n])
