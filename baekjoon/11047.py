# baekjoon s3 동전 0
# https://www.acmicpc.net/problem/11047

import heapq
coin = []
N, K = map(int, input().split())
for _ in range(N):
    heapq.heappush(coin, -int(input()))

result = 0
while coin:
    c = -heapq.heappop(coin)
    result += (K // c)
    K -= (c*(K // c))

print(result)
