# baekjoon s4 괄호
# https://www.acmicpc.net/problem/9012(

import sys
from collections import deque

# 문자열 풀이
N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline()
    while '()' in s:
        s = s.replace('()', '')
    sys.stdout.write('NO\n') if len(s) > 1 else sys.stdout.write('YES\n')

# 스택 풀이
N = int(sys.stdin.readline())

for _ in range(N):
    s = sys.stdin.readline()
    s = s.split('\n')[0]
    stack = deque()
    for i in s:
        stack.appendleft(i)
        if stack[0] == ')' and len(stack) > 1:
            if stack[1] == '(':
                stack.popleft()
                stack.popleft()        
    sys.stdout.write('NO\n') if len(stack) else sys.stdout.write('YES\n')


