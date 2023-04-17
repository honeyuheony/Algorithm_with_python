# baekjoon s1 숨바꼭질
# https://www.acmicpc.net/problem/1697

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = {}
dp[N] = 0
queue = deque()
queue.append(N)
while not K in dp.keys():
    i = queue.popleft()
    if not i+1 in dp.keys() and i+1 <= max(N, K)+1:
        queue.append(i+1)
        dp[i+1] = dp[i]+1
    if not i-1 in dp.keys() and i-1 <= max(N, K)+1:
        queue.append(i-1)
        dp[i-1] = dp[i]+1
    if not i*2 in dp.keys() and i*2 <= max(N, K)+1:
        queue.append(i*2)
        dp[i*2] = dp[i]+1
print(dp[K])
