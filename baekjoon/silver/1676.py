# baekjoon s4 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

import sys
import math
input = sys.stdin.readline

N = int(input())

result = 0
for i in range(1, N+1):
    while i % 5 == 0:
        i /= 5
        result += 1
print(result)
