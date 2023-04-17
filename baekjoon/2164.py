# baekjoon s4 카드2
# https://www.acmicpc.net/problem/2164
# queue
# 시간단축을 위해 O(log n) 수행

import sys
from queue import Queue

N = int(sys.stdin.readline())
card = [i for i in range(1, N+1)]
while len(card) > 1:
    card = [c for index, c in enumerate(card) if index % 2 != 0]
    if N > len(card) * 2:
        temp = card[0]
        del card[0]
        card.append(temp)
    N = len(card)
print(card[0])

