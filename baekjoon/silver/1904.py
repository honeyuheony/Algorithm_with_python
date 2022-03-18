# baekjoon s3 01타일
# https://www.acmicpc.net/problem/1904

N = int(input())
result = 0
dp = [0 for _ in range(N+1)]
if N >= 1:
    dp[1] = 1
if N >= 2:
    dp[2] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] % 15746 + dp[i-2] % 15746
print(dp[N] % 15746)
