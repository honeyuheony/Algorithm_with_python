# baekjoon s2 부분수열의 합
# https://www.acmicpc.net/problem/1182

from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
result = 0
for i in range(1, N+1):
    result += sum([1 for c in combinations(num, i) if sum(c) == S])

print(result)
