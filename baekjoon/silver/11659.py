# baekjoon s3 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline
print = sys.stdout.write

M, N = map(int, input().split())
num = list(map(int, input().split()))
s = [0 for _ in range(len(num))]
temp = 0
for i in range(len(num)):
    temp += num[i]
    s[i] = temp
for _ in range(N):
    start, end = map(int, input().split())
    result = s[len(s)-1]
    if start > 1:
        result -= s[start-2]
    if end < len(num):
        result -= (s[len(s)-1] - s[end-1])
    print(str(result)+'\n')