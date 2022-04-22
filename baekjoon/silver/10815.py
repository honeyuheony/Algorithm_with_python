# baekjoon s4 숫자카드
# https://www.acmicpc.net/problem/10815https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
cards.sort()
M = int(input())
num = list(map(int, input().split()))
result = []

for n in num:
    flag = False
    start = 0
    end = len(cards)-1
    while end-start >= 0:
        mid = (start + end) // 2
        if n == cards[mid]:
            flag = True
            break
        elif n > cards[mid]:
            start = mid+1
        elif n < cards[mid]:
            end = mid-1
    if flag:
        result.append('1')
    else:
        result.append('0')
print(' '.join(result))
