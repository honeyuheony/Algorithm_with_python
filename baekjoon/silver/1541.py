# baekjoon s2 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 1. 문자열을 한글자씩 쪼개 리스트에 담아 탐색하며 연산
# 2-1 + 기호라면 그냥 더하기
# 2-2 - 기호 발견시 그 뒤 +는 모두 -

import sys
input = sys.stdin.readline

f = input().split('\n')[0]
number_list = list(map(int, f.replace('-', ' ').replace('+', ' ').split(' ')))
operator_list = [i for i in list(f) if not i.isnumeric()]
temp = []
flag = False
result = number_list.pop(0)

while len(number_list):
    op = operator_list.pop(0)
    if op == '+':
        if flag:
            result -= number_list.pop(0)
        else:
            result += number_list.pop(0)
    else:
        flag = True
        result -= number_list.pop(0)
print(result)
