# baekjoon s4 제로
# https://www.acmicpc.net/problem/10773

import sys
from collections import deque
N = int(sys.stdin.readline())
count = deque()
for i in range(N):
    k = int(sys.stdin.readline())
    if k == 0:
        count.popleft()
    else:
        count.appendleft(k)
sys.stdout.write(str(sum(count)) + "\n")
