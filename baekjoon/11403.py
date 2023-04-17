# baekjoon s1 경로찾기
# https://www.acmicpc.net/problem/11403

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(0, N):
    graph.append(list(map(int, input().split())))


def dfs(g):
    for k in range(N):
        if graph[g][k] == 1 and visited[k] == 0:
            visited[k] = 1
            dfs(k)


for i in range(0, N):
    visited = [0 for _ in range(N)]
    dfs(i)
    print(' '.join(list(map(str, visited))))
