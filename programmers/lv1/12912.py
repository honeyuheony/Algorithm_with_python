# programmers level1 두 정수 사이의 합
# https://programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    return (a+b) * (abs(b-a)+1) / 2
