# baekjoon s5 나이순정렬
# https://www.acmicpc.net/problem/10814
# 정렬
# 나이, 가입순서
import sys
N = int(sys.stdin.readline())
user_list = []
for i in range(N):
    age, name = sys.stdin.readline().split()
    user_list.append([i, int(age), name])
user_list.sort(key = lambda x: (x[1], x[0]))
for u in user_list:
    sys.stdout.write(str(u[1]) + ' ' + u[2] + '\n')