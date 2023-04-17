# baekjoon s2 로또
# https://www.acmicpc.net/problem/6603

from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    temp = input().split()
    if len(temp) == 1 and temp[0] == '0':
        break
    K = int(temp[0])
    S = temp[1:]
    for c in combinations(S, 6):
        print(' '.join(c))
    print()