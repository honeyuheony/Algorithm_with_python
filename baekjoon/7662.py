# baekjoon g5 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662

import heapq
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    maxheap = []
    minheap = []
    visited = [False for _ in range(1000001)]
    heapsize = 0
    for i in range(N):
        c, n = input().rstrip().split()
        n = int(n)
        if c == 'I':
            heapq.heappush(maxheap, (-n, i))
            heapq.heappush(minheap, (n, i))
            visited[i] = True
        elif c == 'D':
            if n == 1:
                if maxheap:
                    visited[maxheap[0][1]] = False
                    heapq.heappop(maxheap)
            elif n == -1:
                if minheap:
                    visited[minheap[0][1]] = False
                    heapq.heappop(minheap)
            while maxheap and not visited[maxheap[0][1]]:
                heapq.heappop(maxheap)
            while minheap and not visited[minheap[0][1]]:
                heapq.heappop(minheap)
    if maxheap and minheap:
        print(-maxheap[0][0], minheap[0][0])
    else:
        print('EMPTY')
