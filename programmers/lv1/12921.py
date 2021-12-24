# programmers level1 소수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/12921
# 동적계획법
# 효율적인 처리를 위해 i가 이전에 저장한 소수로 나눠지는지 검사
# 1. 1~n 까지의 수 i가 i보다 작은 소수로 나눠지는 지 검사
# 2. sqrt(n)까지의 소수로 나눠지지 않는 수는 소수
import math


def solution(n):
    prime = []
    temp = [i for i in range(2, n+1)]
    while(temp):
        if temp[0] > math.sqrt(n):
            prime += temp
            break
        prime.append(temp[0])
        temp = [i for i in temp if i % temp[0] != 0]
    return len(prime)


print(solution(100))
