'''
programmers level2 올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''
from collections import deque


def solution(s):
    q = deque(s[0])
    for i in range(1, len(s)):
        if not q :
            q.appendleft(s[i])
        elif q[-1] == '(' and s[i] == ')':
            q.pop()
        else:
            q.appendleft(s[i])

    return True if len(q) == 0 else False


print(solution("(())()"))
