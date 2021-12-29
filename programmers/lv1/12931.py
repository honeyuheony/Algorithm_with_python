# programmers level1 자릿수더하기
# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    return sum([int(i) for i in str(n)])


print(solution(123))
