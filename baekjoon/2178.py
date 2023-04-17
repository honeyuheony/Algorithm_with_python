# baekjoon s1 미로 탐색
# https://www.acmicpc.net/problem/2178
# bfs 최적탐색에서 queue, temp를 이용한 풀이시 temp에 넣기전에 방문표시

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append([int(i) for i in input().rstrip()])

queue = deque()
queue.append((0, 0))
result = 0
flag = True
while flag:
    temp = deque()
    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == M-1:
            temp = []
            break
        if 0 < x and matrix[x-1][y]:
            matrix[x-1][y] = 0
            temp.append((x-1, y))
        if x < N-1 and matrix[x+1][y]:
            matrix[x+1][y] = 0
            temp.append((x+1, y))
        if 0 < y and matrix[x][y-1]:
            matrix[x][y-1] = 0
            temp.append((x, y-1))
        if y < M-1 and matrix[x][y+1]:
            matrix[x][y+1] = 0
            temp.append((x, y+1))
    result += 1
    if temp:
        queue = temp
    else:
        flag = False
print(result)
