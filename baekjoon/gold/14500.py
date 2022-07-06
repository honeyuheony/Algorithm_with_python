# baekjoon g5 테트로미노
# https://www.acmicpc.net/problem/14500

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))
tetromino = [
    # ----
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    # --
    # --
    [[0, 0], [1, 0], [0, 1], [1, 1]],
    # -
    # ---
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 0], [0, 1], [0, 2], [1, 0]],
    [[1, 0], [1, 1], [1, 2], [0, 0]],
    [[0, 0], [1, 0], [2, 0], [2, -1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [2, 0], [0, -1]],
    [[0, 0], [1, 0], [2, 0], [0, 1]],
    # --
    #  --
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[0, 0], [0, 1], [-1, 1], [-1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [1, -1], [2, -1]],
    # ---
    #  -
    [[0, 0], [1, -1], [1, 0], [1, 1]],
    [[0, 0], [-1, -1], [-1, 0], [-1, 1]],
    [[0, 0], [-1, -1], [0, -1], [1, -1]],
    [[0, 0], [-1, 1], [0, 1], [1, 1]],
]

max_result = 0
for y in range(N):
    for x in range(M):
        for t in tetromino:
            result = 0
            for dx, dy in t:
                if 0 <= x + dx < M and 0 <= y + dy < N:
                    result += matrix[y+dy][x+dx]
                else:
                    result = -1
                    break
            max_result = max(max_result, result)

print(max_result)
