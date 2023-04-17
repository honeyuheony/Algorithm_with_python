# baekjoon s2 최대힙
# https://www.acmicpc.net/problem/11279
# python의 heapq는 최소힙이다.

import heapq
import sys
input = sys.stdin.readline

h = []
N = int(input())
for _ in range(N):
    i = int(input())
    if i != 0:
        heapq.heappush(h, -i)
    else:
        try:
            sys.stdout.write(str(-heapq.heappop(h)) + '\n')
        except:
            sys.stdout.write('0\n')
