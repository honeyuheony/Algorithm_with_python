# baekjoon s5 수정렬하기2
# https://www.acmicpc.net/problem/2751

import sys
from queue import PriorityQueue
N = int(input())
num_list = PriorityQueue(maxsize=N)
for _ in range(N):
    num_list.put(int(sys.stdin.readline()))
while num_list.qsize():
    sys.stdout.write(str(num_list.get()) + '\n')
