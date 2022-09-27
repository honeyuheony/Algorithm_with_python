'''
baekjoon g5 토마토
https://www.acmicpc.net/problem/7569
'''

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    while q:
        a, b, c = q.popleft()
        visit[c][a][b] = 1
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]
            z = c + dz[i]
            if 0 <= x < n and 0 <= y < m and 0 <= z < h and \
                tomato_matrix[z][x][y] == 0 and visit[z][x][y] == 0:
                q.append([x, y, z])
                tomato_matrix[z][x][y] = tomato_matrix[c][a][b] + 1
                visit[z][x][y] = 1


m, n, h = map(int, input().split())
tomato_matrix = [[] for i in range(h)]
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]
q = deque()
flag = False
st = False
for i in range(h):
    for j in range(n):
        tomato_matrix[i].append(list(map(int, input().split())))
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato_matrix[z][x][y] == 1:
                q.append([x, y, z])
bfs()
max_day = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if tomato_matrix[z][x][y] == 0:
                flag = True
            max_day = max(max_day, tomato_matrix[z][x][y])
print(-1) if flag == True else print(max_day - 1)
    
