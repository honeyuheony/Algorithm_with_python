# programmers level1 내적
# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = sum([a[i] * b[i] for i, _ in enumerate(a)])
    return answer
