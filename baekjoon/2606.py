# baekjoon s3 바이러스
# https://www.acmicpc.net/problem/2606

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
L = int(input())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for _ in range(L):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = deque()
stack.appendleft(1)
result = [1]
while len(stack):
    n = stack.popleft()
    for i in graph[n]:
        if not i in result:
            result.append(i)
            stack.appendleft(i)
print(len(result)-1)

    