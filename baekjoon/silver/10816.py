# baekjoon s4 숫자카드2
# https://www.acmicpc.net/problem/10816
import sys
N = int(sys.stdin.readline())
card_list_1 = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
card_list_2 = list(map(int, sys.stdin.readline().split()))
# 딕셔너리를 통한 풀이
# 1. M개의 찾아볼 숫자를 키로 한 딕셔너리 생성
# 2. N개의 카드더미를 하나씩 pop해 딕셔너리 값 증가
count = {}
for c in card_list_2:
    count[c] = 0
for c in card_list_1:
    try:
        count[c] += 1
    except:
        pass
result = []
for c in card_list_2:
    try:
        result.append(str(count[c]))
    except:
        result.append('0')
sys.stdout.write(' '.join(result) + '\n')
# 이진탐색을 통한 풀이
