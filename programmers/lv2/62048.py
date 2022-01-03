# programmers level2 멀쩡한 사각형
# https://programmers.co.kr/learn/courses/30/lessons/62048
# w * h 개의 정사각형더미에 선을 그었을 때 사용을 못하는 사각형의 개수 세기
# 최대공약수 풀이법 숙지하기
import math


def solution(w, h):
    return w*h - (w+h-math.gcd(w, h))


# Test Code :
print(solution(3, 11))
