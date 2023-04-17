# baekjoon s3 스택 수열
# https://www.acmicpc.net/problem/1874
# 스택
# 1. 1~n까지 push를 수행하며 수열 출력
# 2. n까지 모두 push한 후에 stack 요소를 모두 pop한 결과가 수열의 나머지 결과와 같은지 확인
from collections import deque

N = int(input())
num_list = []
result = []
for i in range(N):
    num_list.append(int(input()))
stack = deque()
index = 0
flag = True
for n in num_list:
    if index < n:
        while index < n:
            index += 1
            stack.appendleft(index)
            result.append('+')
        stack.popleft()
        result.append('-')
    elif index > n:
        if n == stack.popleft():
            result.append('-')
        else:
            flag = False
            print("NO")
            break
if flag:
    for r in result:
        print(r)