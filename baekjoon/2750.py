# baekjoon b1 수 정렬하기
# https://www.acmicpc.net/problem/2750

import sys
input = sys.stdin.readline

N = int(input())
num = []
for _ in range(N):
    num.append(int(input()))

for i in sorted(num):
    print(i)
