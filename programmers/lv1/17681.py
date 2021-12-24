# programmers level1 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
# 1. 각 배열을 복호화해 이차원배열 형태로 저장
# -> 숫자를 이진수로 변환 1 : # 0 : ' '
# 2. 배열을 비교해 하나의 지도 완성
import math


def solution(n, arr1, arr2):
    answer = []
    for a in range(n):
        decode = ''
        for i in range(n-1, -1, -1):
            temp = ' '
            if arr1[a] - math.pow(2, i) >= 0:
                temp = '#'
                arr1[a] -= math.pow(2, i)
            if arr2[a] - math.pow(2, i) >= 0:
                temp = '#'
                arr2[a] -= math.pow(2, i)
            decode += temp
        answer.append(decode)
    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
