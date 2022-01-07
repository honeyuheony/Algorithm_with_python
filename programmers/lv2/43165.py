# programmers level2 타겟 넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
# DFS 깊이 우선 탐색
# 2^len(numbers) 만큼 연산
# 모든 부호 +로 start, 하나씩 음수로 바꿔서 연산 반복
# + - -> + - ++ +- -+ -- ~

depth = 1


def solution(numbers, target):
    global depth
    answer = 0
    if depth == 1 and sum(numbers) == target:
        answer += 1
    a = numbers.copy()
    numbers[depth-1] *= -1
    b = numbers.copy()
    if sum(b) == target:
        answer += 1
    if depth < len(numbers):
        depth += 1
        temp = depth
        answer += solution(a, target)
        depth = temp
        answer += solution(b, target)
    return answer


# Test code
print(solution([1, 1, 1, 1, 1], 5))
