# baekjoon s2 에디터
# https://www.acmicpc.net/problem/1406

from collections import deque
import sys
input = sys.stdin.readline

left = deque(input().rstrip())
right = deque()
N = int(input())
cursor = len(left)
for _ in range(N):
    cmd = input().rstrip()
    if len(cmd) > 1:  # 'P'
        left.append(cmd[2])
    else:
        if cmd[0] == 'L':
            if len(left):
                right.appendleft(left.pop())
        elif cmd[0] == 'D':
            if len(right):
                left.append(right.popleft())
        elif cmd[0] == 'B':
            if len(left):
                left.pop()

print(''.join(left) + ''.join(right))
