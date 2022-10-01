'''
programmers level2 최솟값 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12941
'''


def solution(A, B):
    return sum([a*b for a, b in zip(sorted(A), sorted(B, reverse=True))])


print(solution([1, 4, 2], [5, 4, 4]))
