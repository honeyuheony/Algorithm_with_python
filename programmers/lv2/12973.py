# programmers level2 짝지어 제거하기
# https://programmers.co.kr/learn/courses/30/lessons/12973
# 문자열, 스택
# 1. 2 반복
# 1. 각 문자열을 하나씩 떼어 스택에 push
# 2. 스택의 0번째, 1번째 값이 같으면 pop
# 결과 스택의 길이가 0이면 성공, 아니면 실패
# !! 대량의 문자열, list 연산시 stack, queue등의 자료구조 사용 생각하기

from queue import deque


def solution(s):
    stack = deque()
    for i in s:
        stack.appendleft(i)
        try:
            if stack[0] == stack[1]:
                stack.popleft()
                stack.popleft()
        except:
            continue
    return 1 if len(stack) == 0 else 0


# Test code:
s = "abcdefg"*10000 + "gfedcba"*10000 + "abcdefg"*10000 + "gfedcba"*10000

print(solution(s))
