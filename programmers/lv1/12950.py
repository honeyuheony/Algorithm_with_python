# programmers level1 행렬의 덧셈
# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    return [[m+n for m, n in zip(a, b)]for a, b in zip(arr1, arr2)]
