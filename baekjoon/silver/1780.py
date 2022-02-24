# baekjoon s2 종이의 개수
# https://www.acmicpc.net/problem/1780

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    m = list(map(int, input().split()))
    matrix.append(m)


def check(x, y, l):
    s = matrix[x][y]
    flag = False
    if l == 1:
        result[s+1] += 1
    else:
        for i in range(x, x+l):
            for j in range(y, y+l):
                if s != matrix[i][j]:
                    flag = True
                    break
        if not flag:
            result[s+1] += 1
        else:
            for i in range(x, x+l, l//3):
                for j in range(y, y+l, l//3):
                    check(i, j, l//3)


result = [0, 0, 0]
check(0, 0, len(matrix))

for r in result:
    print(r)
