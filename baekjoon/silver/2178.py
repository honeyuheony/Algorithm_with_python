# baekjoon s1 미로 탐색
# https://www.acmicpc.net/problem/2178

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
        print(x, y)
        if x == N-1 and y == M-1:
            temp = []
            break
        matrix[x][y] = 0
        if 0 < x and matrix[x-1][y]:
            temp.append((x-1, y))
        if x < N-1 and matrix[x+1][y]:
            temp.append((x+1, y))
        if 0 < y and matrix[x][y-1]:
            temp.append((x, y-1))
        if y < M-1 and matrix[x][y+1]:
            temp.append((x, y+1))
    result += 1
    if temp:
        queue = temp
    else:
        flag = False
print(result)
