# baekjoon b1 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

import sys
import math
a, b, t = map(int, sys.stdin.readline().split())
if a >= t:
    print(1)
else:
    result = math.ceil((t-a) / (a-b)) + 1
    print(result)