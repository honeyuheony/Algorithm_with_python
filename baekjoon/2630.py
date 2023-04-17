# baekjoon s3 색종이 만들기
# https://www.acmicpc.net/problem/2630
# 1. 색종이를 꺼내 색종이가 모두 동일한 색인지 검사
# 2. 아니라면 4등분해서 다시 queue에 넣기
# 3. 맞다면 색깔 카운트

from collections import deque
import sys
from math import sqrt
input = sys.stdin.readline

N = int(input())
paper = []
temp = []
for i in range(N):
    r = list(map(int, input().split()))
    for j in r:
        temp.append(j)
paper.append(temp)

blue = 0
white = 0
while len(paper):
    p = paper.pop(0)
    s = sum(p)
    if s == 0:
        white += 1
    elif s == len(p):
        blue += 1
    else:
        temp = [[], [], [], []]
        for index, i in enumerate(p):
            if index < len(p) // 2:
                if index % sqrt(len(p)) < sqrt(len(p)) // 2:
                    temp[0].append(i)
                else:
                    temp[1].append(i)
            else:
                if index % sqrt(len(p)) < sqrt(len(p)) // 2:
                    temp[2].append(i)
                else:
                    temp[3].append(i)
        for t in temp:
            paper.append(t)
print(white)
print(blue)
