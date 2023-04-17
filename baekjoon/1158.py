# baekjoon s4 요세우스 문제
# https://www.acmicpc.net/problem/1158

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
circle = deque([i for i in range(1, N+1)])
result = []
while circle:
    for i in range(K-1):
        circle.append(circle.popleft())
    result.append(str(circle.popleft()))
print('<' + ', '.join(result) + '>')
