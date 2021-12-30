# programmers level 하샤드 수
# https://programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수 : 자릿수의 합으로 나누어지는 양의 정수

def solution(x):
    return False if x % sum(list(map(int, str(x)))) else True


print(solution(17))
