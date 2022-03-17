# baekjoon s1 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
absheap = []
for _ in range(N):
    i = int(input())
    if i == 0:
        if absheap:
            r = heapq.heappop(absheap)
            r = r[0] if r[1] else -r[0]
            print(str(r) + '\n')
        else:
            print('0\n')
    else:
        plus = True if i > 0 else False
        heapq.heappush(absheap, (abs(i), plus))
