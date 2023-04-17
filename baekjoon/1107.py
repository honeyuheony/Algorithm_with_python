# baekjoon g5 리모컨
# https://www.acmicpc.net/problem/1107

import math
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
break_btn = list(map(int, input().split()))
btn = [i for i in range(10) if i not in break_btn]

high_nearby = math.inf
low_nearby = math.inf
if set([int(i) for i in str(N)]) & set(break_btn):
    for i in range(N+1, 1000000):
        if not set([int(s) for s in str(i)]) & set(break_btn):
            high_nearby = i
            break
    for i in range(N-1, -1, -1):
        if not set([int(s) for s in str(i)]) & set(break_btn):
            low_nearby = i
            break
    print(min(len(str(high_nearby)) + high_nearby - N,
          len(str(low_nearby)) + abs(low_nearby-N), abs(N-100)))
else:
    print(min(len(str(N)), abs(N-100)))
