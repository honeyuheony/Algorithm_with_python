# baekjoon b3 직각삼각형
# https://www.acmicpc.net/problem/4153
# 수학
import sys

while True:
    lines = list(map(int, sys.stdin.readline().split()))
    if sum(lines) <= 0:
        break
    m = max(lines)
    lines.remove(m)
    print("right") if pow(lines[0], 2) + pow(lines[1], 2) == pow(m, 2) \
        else print("wrong")