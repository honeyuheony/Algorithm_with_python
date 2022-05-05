# baekjoon g5 N-Queen
# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

N = int(input())
queens = []
depth = 1
block_row = []
result = 0


def dfs(queens, depth, block_row, result):
    temp_block_row = set()
    for index, q in enumerate(reversed(queens)):
        if q[0] - (index+1) >= 0:
            temp_block_row.add(q[0] - (index+1))
        if q[0] + (index+1) <= N:
            temp_block_row.add(q[0] + (index+1))
    temp_block_row = list(temp_block_row) + block_row
    open_row = [i for i in range(1, N+1) if i not in temp_block_row]

    for row in open_row:
        if depth == N:
            result += 1
        else:
            result = dfs(queens + [(row, depth)],
                         depth+1, block_row + [row], result)
    return result

print(dfs(queens, depth, block_row, result))