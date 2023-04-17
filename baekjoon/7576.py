# baekjoon g5 토마토
# https://www.acmicpc.net/problem/7576

from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
tomato = []
for _ in range(N):
    tomato.append(list(map(int, input().split())))
result = 0
queue = deque()
temp = deque()
unripe = 0
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i, j))
        elif tomato[i][j] == 0:
            unripe += 1
while unripe:
    while queue:
        i, j = queue.popleft()
        if 0 <= i+1 < N:
            if tomato[i+1][j] == 0:
                tomato[i+1][j] = 1
                temp.append((i+1, j))
                unripe -= 1
        if 0 <= i-1 < N:
            if tomato[i-1][j] == 0:
                tomato[i-1][j] = 1
                temp.append((i-1, j))
                unripe -= 1
        if 0 <= j+1 < M:
            if tomato[i][j+1] == 0:
                tomato[i][j+1] = 1
                temp.append((i, j+1))
                unripe -= 1
        if 0 <= j-1 < M:
            if tomato[i][j-1] == 0:
                tomato[i][j-1] = 1
                temp.append((i, j-1))
                unripe -= 1
    if unripe > 0 and not temp:
        result = -1
        break
    else:
        queue = temp
        temp = deque()
        result += 1
print(result)
