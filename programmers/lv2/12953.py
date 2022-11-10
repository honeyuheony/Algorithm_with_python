'''
programmers lv2 N개의 최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953#
'''

import math


def solution(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans * arr[i] // math.gcd(ans, arr[i])
    return ans