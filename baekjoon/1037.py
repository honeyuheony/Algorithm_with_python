# baekjoon s5 약수
# https://www.acmicpc.net/problem/1037

import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
print(max(num_list) * min(num_list))
