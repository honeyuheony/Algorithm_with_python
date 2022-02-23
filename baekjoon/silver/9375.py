# baekjoon s3 패션왕 신해빈
# https://www.acmicpc.net/problem/9375
# 집합 경우의수 구하기 = 각 원소 개수 + 1 해서 전부 곱하고 -1

from functools import reduce
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    clothes = {}
    for _ in range(N):
        name, category = input().rstrip().split()
        try:
            clothes[category] += 1
        except:
            clothes[category] = 0
            clothes[category] += 1
    result = 1
    for c in clothes.values():
        result *= c+1
    print(result-1)
            