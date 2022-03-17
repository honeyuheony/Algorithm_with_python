# baekjoon s1 카잉 달력
# https://www.acmicpc.net/problem/6064

import math
import sys
import time
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    lcm = (M*N)//math.gcd(M, N)+1
    flag = True
    for i in range(y, lcm+1, N):
        if (i-x) % M == 0:
            print(i)
            flag = False
    if flag:
        print(-1)
