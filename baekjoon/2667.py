# baekjoon s1 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append([int(i) for i in input().rstrip()])
visited = [[0]*N for _ in range(N)]
result = []


def dfs(i, j, matrix, visited):
    matrix[i][j] = 0
    visited[i][j] = 1
    global count
    count += 1
    if 0 < i and matrix[i-1][j] == 1:
        dfs(i-1, j, matrix, visited)
    if i < N-1 and matrix[i+1][j] == 1:
        dfs(i+1, j, matrix, visited)
    if 0 < j and matrix[i][j-1] == 1:
        dfs(i, j-1, matrix, visited)
    if j < N-1 and matrix[i][j+1] == 1:
        dfs(i, j+1, matrix, visited)


for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            count = 0
            dfs(i, j, matrix, visited)
            result.append(count)
result.sort()
print(len(result))
for r in result:
    print(r)
