# programmers level2 수식최대화
# https://programmers.co.kr/learn/courses/30/lessons/17677
from itertools import permutations
import operator as Oper
from collections import deque
from copy import deepcopy

def solution(expression):
    '''
    1. 수식에서 연산자의 종류 개수 세기, 숫자와 연산자로 이루어진 elements deque 생성
    2. n! 개의 연산자 우선순위 리스트로 반복문 돌리기
    2-1. elements deque copy, new_deque 생성
    2-2. 큐에서 숫자하나, 연산자 하나 꺼내기 => 연산자가 현재 계산할 순서라면 숫자 하나 더 꺼낸뒤 연산, copy deque 맨 앞에 결과 삽입
                                        계산할 순서가 아니라면 new_deque에 숫자와 연산자 순서대로 삽입
    2-3. 해당 연산자가 deque에 없다면 다음 연산자로 반복문 수행
    3. copy deque가 비면 종료, new_deque에 최종값을 max_result에 비교해 결과 삽입
    '''
    operation_set = set()
    elements = deque()
    element = ''
    for index, e in enumerate(expression):
        if e.isdigit():
            element += e
            if index == len(expression)-1:
                elements.append(element)
        else:
            elements.append(element)
            elements.append(e)
            operation_set.add(e)
            element = ''
    
    def calculation(x, y, oper):
        ops = { "+": Oper.add, "-": Oper.sub, '*': Oper.mul}
        return ops[oper](x, y)

    max_result = 0
    operation_rank_list = permutations(operation_set, len(operation_set))
    for operation_rank in operation_rank_list:
        copy_elements = deepcopy(elements)
        new_elements = deque()
        for operator in operation_rank:
            while copy_elements:
                x = copy_elements.popleft()
                if copy_elements:
                    oper = copy_elements.popleft()
                    if operator == oper:
                        y = copy_elements.popleft()
                        copy_elements.appendleft(str(calculation(int(x), int(y), operator)))
                    else:
                        new_elements.append(x)
                        new_elements.append(oper)
                else:
                    new_elements.append(x)
            copy_elements = new_elements
            new_elements = deque()
        max_result = max(max_result, abs(int(copy_elements.pop())))
    return max_result
            
print(solution('100-200*300-500+20'))