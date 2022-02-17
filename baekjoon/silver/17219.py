# baekjoon s4 비밀번호 찾기
# https://www.acmicpc.net/problem/17219
# 해싱

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
passwd_dict = {}
for i in range(N):
    key, value = input().replace('\n', '').split()
    passwd_dict[key] = value

for i in range(M):
    key = input().replace('\n', '')
    sys.stdout.write(passwd_dict[key] + '\n')
