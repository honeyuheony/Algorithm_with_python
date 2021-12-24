# programmers level1 나누어 떨어지는 숫자 배열
# https://programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = []
    for a in arr:
        if not a % divisor:
            answer.append(a)
    answer.sort()
    if not len(answer):
        answer.append(-1)
    return answer
    # return [a for a in arr if not a % divisor] or [-1]
