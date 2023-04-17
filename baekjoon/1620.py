# baekjoon s4 포켓몬마스터 이다솜
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
book = {}
book_reverse = {}

for i in range(1, M+1):
    s = input().rstrip()
    book[i] = s
    book_reverse[s] = i


for i in range(N):
    s = input().rstrip()
    if s.isdigit():
        sys.stdout.write(book[int(s)] + '\n')
    else:
        sys.stdout.write(str(book_reverse[s]) + '\n')
