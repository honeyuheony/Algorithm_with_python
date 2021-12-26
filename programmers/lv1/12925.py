# programmers level1 문자열을 정수로 바꾸기
# https://programmers.co.kr/learn/courses/30/lessons/12925
import re


def solution(s):
    answer = int(re.compile('[0-9]+').findall(s)[0])
    if s[0] == '-':
        answer = -answer
    return answer
