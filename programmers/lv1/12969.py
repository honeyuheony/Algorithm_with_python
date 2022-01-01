# programmers level1 직사각형 별찍기
# https://programmers.co.kr/learn/courses/30/lessons/12969

a, b = map(int, input().strip().split(' '))
line = ''.join(['*' for _ in range(a)])
for _ in range(b):
    print(line)
