# baekjoon s1 쿼드트리
# https://www.acmicpc.net/problem/1992

import sys
input = sys.stdin.readline

matrix = []
N = int(input())
for _ in range(N):
    matrix.append([int(i) for i in input().rstrip()])
result = ''


def devide_conquer(matrix):
    global result
    if sum([sum(m) for m in matrix]) == len(matrix)**2:
        result = result + '1'
    elif sum([sum(m) for m in matrix]) == 0:
        result = result + '0'
    else:
        result = result + '('
        devide_matrix = [[], [], [], []]
        for m in range(len(matrix)):
            temp = [[], [], [], []]
            for n in range(len(matrix)):
                if 0 <= m < len(matrix)//2 and 0 <= n < len(matrix)//2:
                    temp[0].append(matrix[m][n])
                elif 0 <= m < len(matrix)//2 and len(matrix)//2 <= n:
                    temp[1].append(matrix[m][n])
                elif len(matrix)//2 <= m and 0 <= n < len(matrix)//2:
                    temp[2].append(matrix[m][n])
                else:
                    temp[3].append(matrix[m][n])
            for i in range(len(devide_matrix)):
                if temp[i]:
                    devide_matrix[i].append(temp[i])
        for i in range(len(devide_matrix)):
            devide_conquer(devide_matrix[i])
        result = result + ')'


devide_conquer(matrix)
print(result)
