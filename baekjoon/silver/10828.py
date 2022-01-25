# baekjoon s4 스택
# https://www.acmicpc.net/problem/10828

from collections import deque
import sys
N = int(sys.stdin.readline())
stack = deque()
for _ in range(N):
    command = sys.stdin.readline().replace('\n', '')
    if ' ' in command:
        command, item = command.split()
        item = int(item)
    if command == 'push':
        stack.appendleft(item)
    elif command == 'pop':
        try:
            t = stack.popleft()
        except:
            t = -1
        sys.stdout.write(str(t) + '\n')
    elif command == 'size':
        t = len(stack)
        sys.stdout.write(str(t) + '\n')
    elif command == 'empty':
        t = 0 if len(stack) else 1
        sys.stdout.write(str(t) + '\n')
    elif command == 'top':
        t = stack[0] if len(stack) else -1
        sys.stdout.write(str(t) + '\n')