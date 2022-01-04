# programmers level2 124나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899
# 수학, 구현
# 자릿수 : n > ∑(3^i) 을 만족하는  i
# 각 숫자 : 십진수 - k(3^i) > 0을 만족하는 k
# 각 자릿수는 10진법의 해당 자릿수를 3^자릿수로 나눈 값이다.
# 11 : 4 / 111 : 13 / 1111 : 40 = 27 + 9 + 3 + 1

import math


def solution(n):
    answer = ''
    answer_length = 0
    temp = 0
    digits = [0]
    while(True):
        temp += pow(3, answer_length)
        if n >= temp:
            digits.append(temp)
            answer_length += 1
        else:
            break
    while(answer_length > 0):
        k = (n - digits[answer_length-1]) // pow(3, answer_length-1)
        n -= k * pow(3, answer_length-1)
        if k == 3:
            k = 4
        answer += str(k)
        answer_length -= 1
    return answer


# Test Code
print(solution(3))
