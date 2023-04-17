# baekjoon s5 중복 빼고 정렬하기
# https://www.acmicpc.net/problem/10867

import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num_dict = {}
for i in num:
    if not i in num_dict:
        num_dict[i] = 1
for i in sorted(num_dict.keys()):
    print(i, end=' ')
