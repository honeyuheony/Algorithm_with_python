'''
programmers level2 다음 큰 숫자
https://school.programmers.co.kr/learn/courses/30/lessons/12911
'''
def solution(n):
    c = bin(n)[2:].count('1')
    while True:
        n += 1
        if bin(n)[2:].count('1') == c:
            return n