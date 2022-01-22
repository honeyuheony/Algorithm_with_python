# baekjoon b2 블랙잭
# https://www.acmicpc.net/problem/2798
# 조합, 브루트포스

import itertools
import sys

n, m = map(int, input().split())
card = map(int, sys.stdin.readline().split())

selected = [sum(s) for s in itertools.combinations(card, 3) if sum(s) <= m]
print(max(selected))
