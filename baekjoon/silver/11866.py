'''
baekjoon s5 요세우스 문제 0
https://www.acmicpc.net/problem/11866
'''

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
circle_num = deque([i for i in range(1, N+1)])
permutation = []

while circle_num:
    for i in range(K-1):
        temp = circle_num.popleft()
        circle_num.append(temp)
    permutation.append(str(circle_num.popleft()))
print(f"<{', '.join(permutation)}>")
