# baekjoon s2 유기농배추
# https://www.acmicpc.net/problem/1012
# dfs
# 1. 배추가 심어진 위치 리스트 생성
# 2. 배추 하나를 골라 상하좌우로 다른 배추가 있는지 검사
# -> 있다면 계속 주변 탐색
# -> 찾은 모든 배추 다 반환, count 1 증가
#########################################
# 크기가 5x5인 2차원배열의 [-1][4] 인덱스로 접근하면 에러가 나지 않고 [4][4] 로 접근한다.

import sys
sys.setrecursionlimit(100000)


def cabbage_dfs(x, y):
    matrix[y][x] = 0
    cabbage.remove((x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N:
            c = matrix[y+dy[i]][x+dx[i]]
            if c == 1:
                cabbage_dfs(x+dx[i], y+dy[i])


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    cabbage = []
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        cabbage.append((x, y))
        matrix[y][x] = 1
    count = 0
    while len(cabbage):
        x, y = cabbage[0]
        count += 1
        cabbage_dfs(x, y)
    sys.stdout.write(str(count) + '\n')
