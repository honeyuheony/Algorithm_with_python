# baekjoon b1 펠린드롬수
# https://www.acmicpc.net/problem/1259
# 문자열, 구현
# 1. 가운데 문자를 기준으로 왼쪽 문자열과 오른쪽문자열을 뒤집은 값을 비교

while True:
    i = input()
    if i == '0':
        break
    middle = len(i)//2
    print('yes') if i[0:middle] == i[len(i)-1:len(i)-middle-1:-1] else print('no')