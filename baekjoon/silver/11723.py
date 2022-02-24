# baekjoon s5 집합
# https://www.acmicpc.net/problem/11723
# 집합, 비트마스킹

import time
import sys
# 집합
input = sys.stdin.readline

s = set()
all = set([str(i) for i in range(1, 21)])
N = int(input())
for _ in range(N):
    op = input().rstrip()
    if ' ' in op:
        op, x = op.split()
    if op == 'add':
        s.add(x)
    elif op == 'remove':
        s.discard(x)
    elif op == 'check':
        sys.stdout.write('1\n' if s.issuperset(set([x])) else '0\n')
    elif op == 'toggle':
        s.discard(x) if s.issuperset(set([x])) else s.add(x)
    elif op == 'all':
        s = all
    elif op == 'empty':
        s.clear()

# 비트마스킹
s = 0b00000000000000000000
all = set([str(i) for i in range(1, 21)])
N = int(input())
for _ in range(N):
    op = input().rstrip()
    if ' ' in op:
        op, x = op.split()
        x = int(x)
    if op == 'add':
        s = s | (1 << x-1)
    elif op == 'remove':
        s = s & ~(1 << x-1)
    elif op == 'check':
        if s & (1 << x-1) == (1 << x-1):
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif op == 'toggle':
        s = s ^ (1 << x-1)
    elif op == 'all':
        s = 0b11111111111111111111
    elif op == 'empty':
        s = 0b00000000000000000000
