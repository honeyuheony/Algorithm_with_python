# baekjoon s3 ATM
# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline


N = int(input())
p = list(map(int, input().split()))
p.sort()
result = 0
for i in range(1, N+1):
    result += sum(p[0:i])
print(result)