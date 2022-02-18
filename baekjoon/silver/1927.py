# baekjoon s2 최소힙
# https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

h = []
T = int(input())
for _ in range(T):
    n = int(input())
    if n == 0:
        try:
            print(heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, n)
