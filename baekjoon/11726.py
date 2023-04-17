# baekjoon s3 2xn 타일링
# https://www.acmicpc.net/problem/11726
# 9c0 + 8c1 + 7c2 + 6c3 + 5c4 = 1 + 8 + 21 + 20 + 5 = 55
# 8c0 + 7c1 + 6c2 + 5c3 + 4c4

from itertools import combinations
from math import comb
import sys
input = sys.stdin.readline

n = int(input())
result = 0
i = 0
while i <= n//2:
    temp = 1
    for k in range(0, i):
        temp = temp*(n-i-(k)) // (k+1)
    result += temp
    i += 1
print(result % 10007)
