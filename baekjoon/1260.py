# baekjoon s2 dfs 와 bfs
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M, V = map(int, input().split())
graph = {}
for n in range(1, N+1):
    graph[n] = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
result = []
current = V
result.append(current)
stack = deque()
for i in sorted(graph[current]):
    stack.append(i)
while stack and len(result) < N:
    current = stack.popleft()
    result.append(current)
    next_g = sorted([i for i in graph[current]
                if not i in result], reverse=True)
    for i in next_g:
        if i in stack:
            stack.remove(i)
        stack.appendleft(i)
        
result = ' '.join(map(str, result))
print(result)

# BFS
result = []
current = V
result.append(current)
stack = deque()
for i in sorted(graph[current]):
    stack.append(i)
while stack and len(result) < N:
    current = stack.popleft()
    result.append(current)
    next_g = sorted([i for i in graph[current]
            if not i in result])
    for i in next_g:
        if not i in stack:
            stack.append(i)
result = ' '.join(map(str, result))
print(result)
    