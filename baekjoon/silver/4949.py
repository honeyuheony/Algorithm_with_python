# baekjoons s4 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
# 문자열, 큐
# 1. 문자열을 하나씩 뽑는다.
# 2. 뽑은 문자가 괄호인지 검사한다.
# 3. 스택이 비어있지않다면 뽑은 괄호와 스택의 첫번째 값이 같은지 검사한다.
# 4. 같다면 첫번째 값 pop, 다르다면 뽑은 문자를 put
# 5. 종료 후 스택의 길이가 0이라면 yes 아니면 no
import sys
from collections import deque

while True:
    string = sys.stdin.readline()
    if string == '.\n':
        break
    string = list(string)
    string.remove('\n')
    stack = deque()
    parenthesis = ['(', ')', '[', ']']
    while len(string):
        p = string.pop(0)
        if not p in parenthesis:
            continue
        if not len(stack):
            stack.appendleft(p)
        else:
            if p == ')' and stack[0] == '(' or p == ']' and stack[0] == '[': 
                stack.popleft()
            else:
                stack.appendleft(p)
    if len(stack):
        sys.stdout.write('no\n')
    else:
        sys.stdout.write('yes\n')
        