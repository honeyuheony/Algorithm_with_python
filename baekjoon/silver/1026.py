# baekjoon s4 보물
# https://www.acmicpc.net/problem/1026

from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
A = deque(sorted(map(int, input().split())))
B = deque(sorted(map(int, input().split())))

result = 0
while A:
    result += A.pop() * B.popleft()
print(result)
