# baekjoon g5 AC
# https://www.acmicpc.net/problem/5430

from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    command = input().rstrip()
    N = int(input())
    num_list = input().rstrip()
    if len(num_list[1:len(num_list)-1]) != 0:  # 입력 배열이 빈 배열이 아닌경우
        num_list = deque(num_list[1:len(num_list)-1].split(','))
        result = ''
        reverse = False
        command = command.split('R')
        for index, c in enumerate(command):
            try:
                if not reverse:
                    for _ in range(len(c)):
                        num_list.popleft()
                else:
                    for _ in range(len(c)):
                        num_list.pop()
                if index < len(command)-1:  # 뒤에 D 묶음이 더 있다 -> 뒤집기
                    reverse = not reverse
            except:  # D 연산에서 오류 발생시
                result = 'error'
                break
        if result == '':
            if reverse:
                num_list.reverse()
            result = '[' + ','.join(num_list) + ']'
        print(result)
    else:
        if 'D' in command:
            print('error')
        else:
            print([])
