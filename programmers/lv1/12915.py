# programmers level1 문자열 내 맘대로 정렬하기
# https://programmers.co.kr/learn/courses/30/lessons/12915
# sort의 key로 람다함수 다중인자가 가능하다.

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


print(solution(["abce", "abcd", "cdx"], 1))
