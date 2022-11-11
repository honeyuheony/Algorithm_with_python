'''
programmers lv2 예상대진표
https://school.programmers.co.kr/learn/courses/30/lessons/12985#
'''

def solution(n,a,b):
    answer = 1
    a, b = min(a, b), max(a, b)
    ans = 1
    while (a+1) // 2 != (b+1) // 2:
        a = (a+1) // 2
        b = (b+1) // 2
        ans += 1
    return ans