# programmers level1 제일 작은 수 제거
# https://programmers.co.kr/learn/courses/30/lessons/12935
# 탐색 문제

def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) else [-1]
