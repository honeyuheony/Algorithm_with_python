# baekjoon g3 연료채우기
# https://www.acmicpc.net/problem/1826
import sys
import heapq
from collections import deque

input = sys.stdin.readline

N = int(input())
oil_bank = []
for i in range(N):
    a, b = map(int, input().split())
    oil_bank.append([a, -b])  # 최대 힙을 위해 기름량 음수로 저장
oil_bank.sort(key=lambda x: x[0])
oil_bank = deque(oil_bank)
L, P = map(int, input().split())


# 남은 오일 중 갈 수 있는 가장 용량 큰 주유소로 이동
# 현재 갈 수 있는 주유소가 없다면 이전 주유소 목록 그리디 탐색
# cnt = 0
result = 0
cur_distance, cur_oil = 0, P
bank_heap = []
while cur_distance + cur_oil < L:
    while len(oil_bank):
        o = oil_bank.popleft()
        if cur_distance + cur_oil >= o[0]:
            heapq.heappush(bank_heap, (o[1], o[0]))
        else:
            oil_bank.appendleft(o)
            break
    if len(bank_heap):
        greedy = heapq.heappop(bank_heap)  # [0] 거리, [1] 기름량
        cur_oil -= greedy[1] - cur_distance
        cur_distance += greedy[1] - cur_distance
        cur_oil += -greedy[0]
        result += 1
    else:
        result = -1
        break

print(result)
