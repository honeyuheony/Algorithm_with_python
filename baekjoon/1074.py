# baekjoon s1 Z
# https://www.acmicpc.net/problem/1074
# 1. 자신의 위치가 몇 사분면인지 나열
# 2. 사분면 총 사각형 개수 * (자신의 사분면-1 / 4) 를 반복 계싼


import sys
input = sys.stdin.readline
N, r, c = map(int, input().split())
max = pow(2, N)
quadrant = []
x, y = c+1, r+1
while max > 1:
    if y <= max // 2:
        if x <= max // 2:
            q = 1
        else:
            q = 2
    else:
        if x <= max // 2:
            q = 3
        else:
            q = 4
    max = max // 2
    if x > max:
        x -= max
    if y > max:
        y -= max
    quadrant.append(q)

result = 0
while quadrant:
    temp = pow(4, len(quadrant))
    q = quadrant.pop(0)
    result += temp * (q-1) / 4
print(int(result))
