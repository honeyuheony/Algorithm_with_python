# baekjoon s5 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
num = {}
for i in range(N):
    k = int(input())
    if k in num.keys():
        num[k] += 1
    else:
        num[k] = 1

for i in sorted(num.keys()):
    for _ in range(num[i]):
        print(str(i) + '\n')
