# baekjoon s5 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
# 브루트포스
# 1. (0, 0)부터 (n-7, m-7)칸까지 시작점 선정
# 2. 시작점부터 8칸까지 각 행이 체스판을 이루는데 칠해야하는 숫자 구하기
# 3. 구간의 최소합 구하기
import math
n, m = map(int, input().split())
matrix = []
result = []
sol = [['W' if (i+j)%2 else 'B' for j in range(m)]for i in range(n)]
for row in range(n):
    col = input()
    matrix.append(col)
for r in range(n):
    temp = []
    for c in range(m):
        t = 1 if matrix[r][c] == sol[r][c] else 0
        temp.append(t)
    result.append(temp)
s = math.inf
for r in range(n-7):
    for c in range(m-7):
        type1 = 0
        type2 = 0
        for a in range(8):
            type1 += sum(result[r+a][c:c+8])
            type2 += 8-sum(result[r+a][c:c+8])
        if s > type1 :
            s = type1
        if s > type2 :
            s = type2
print(s)