# baekjoon g5 적록색약
# https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

img = []
N = int(input())
for i in range(N):
    img.append(input().strip())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, color):
    if visited[y][x] == 1 or img[y][x] != color:
        return 0
    else:
        visited[y][x] = 1
        for i in range(4):
            next_x = x + dx[i] 
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                dfs(next_x, next_y, img[y][x])

def dfs_blindness(x, y, color):
    color_same = ['R', 'G']
    if visited[y][x] == 0 and (color == img[y][x] or (color in color_same and img[y][x] in color_same)):
        visited[y][x] = 1
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < N:
                dfs_blindness(next_x, next_y, img[y][x])
        


result = [0, 0]
visited = [[0] * N for i in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            dfs(x, y, img[y][x])
            result[0] += 1

visited = [[0] * N for i in range(N)]
for y in range(N):
    for x in range(N):
        if visited[y][x] == 0:
            dfs_blindness(x, y, img[y][x])
            result[1] += 1

print(result[0], result[1])

        

    
    