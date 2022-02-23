# baekjoon s4 듣보잡
# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

listen = []
see = []
for _ in range(N):
    listen.append(input().rstrip())
for _ in range(M):
    see.append(input().rstrip())
result = set(listen) & set(see)
print(len(result))
for r in sorted(result):
    print(r)
