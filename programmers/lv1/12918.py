# programmers level1 문자열 다루기 기본
# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    return len(s) in (4, 6) and s.isnumeric()
