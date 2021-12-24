# programmers level1 문자열 내 p와 y의 개수
# https://programmers.co.kr/learn/courses/30/lessons/12916
# 정규식 사용 p와 y 추출 개수 비교
import re


def solution(s):
    p = re.compile('p|P')
    y = re.compile('y|Y')
    answer = len(p.findall(s)) == len(y.findall(s))
    print(s.count('p'))
    return answer


print(solution('pPoooyY'))
