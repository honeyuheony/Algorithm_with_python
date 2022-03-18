# baekjoon s3 2xn 타일링 2
# https://www.acmicpc.net/problem/11727
n = int(input())
result = 0
dp = [0 for _ in range(n+1)]
if n >= 1:
    dp[1] = 1
if n >= 2:
    dp[2] = 3
for i in range(3, n+1):
    dp[i] = dp[i-1] % 10007 + 2*dp[i-2] % 10007

print(dp[n] % 10007)
