# baekjoon s1 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928
# 단방향 그래프, BFS
# 큐가 비워질 때까지 큐에서 하나씩 꺼내
# 1. 해당 칸에 도착한 적 있다면 스킵
# 2. 칸에 방문표시, 칸에 뱀이나 사다리 연결되있다면 연결칸 queue 삽입
# 3. 해당칸에서 이동할 수 있는 모든 칸 temp에 삽입
# 4. 큐가 비면 count += 1 후 queue에 temp 데이터 삽입

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
snake = {}
ladder = {}

for _ in range(N):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    snake[x] = y

matrix = [0 for i in range(101)]
queue = [1]
count = 0
while True:
    temp = []
    flag = False
    while len(queue):
        s = queue.pop(0)
        if matrix[s] == 0:
            matrix[s] = 1
            if s in ladder.keys():
                queue.append(ladder[s])
            elif s in snake.keys():
                queue.append(snake[s])
            else:
                for i in range(1, 7):
                    if s + i == 100:
                        flag = True
                        break
                    temp.append(s+i)
    queue = temp
    count += 1
    if flag:
        print(count)
        break
