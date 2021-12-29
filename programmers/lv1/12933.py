# programmers level1 정수 내림차순으로 배치하기
# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정렬문제

def solution(n):
    return int(''.join(sorted([i for i in str(n)], reverse=True)))


print(solution(12732))
