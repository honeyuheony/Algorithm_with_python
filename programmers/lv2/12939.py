'''
programmers level2 최댓값과 최솟값
https://school.programmers.co.kr/learn/courses/30/lessons/12939
'''


def solution(s):
    l = list(map(int, s.split()))
    return f'{min(l)} {max(l)}'


print(solution("-1 -2 -3 -4"))
