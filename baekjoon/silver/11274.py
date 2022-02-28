# baekjoon s2 연결 요소의 개수
# https://www.acmicpc.net/problem/11724
# 1. dfs로 각 정점에서 갈 수 있는 최대 깊이까지 도달한 뒤 지나간 정점을 담은 list 저장
# 2. 리스트끼리 비교해 포함관계 제거 후 카운트

from collections import deque
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = {}
for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(dot, visited):
    visited.append(dot)
    for g in graph[dot]:
        if not g in visited:
            dfs(g, visited)


result = 0
visited = []
for i in range(1, N+1):
    if not i in visited:
        result += 1
        dfs(i, visited)

print(result)
