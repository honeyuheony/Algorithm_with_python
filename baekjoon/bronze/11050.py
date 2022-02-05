# baekjoon b1 이항계수
# https://www.acmicpc.net/problem/11050

import sys
from itertools import combinations

N, K = map(int, sys.stdin.readline().split())
s = 'a' * N
sys.stdout.write(str(len(list(combinations(s, K)))) + '\n')
