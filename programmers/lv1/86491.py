# programmers level1 최소직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491
# 모든 명함의 사이즈를 정렬하면 문제 해결이 가능하다.
# 연산을 더 적게 하기 위해 필요한 명함만 가로세로 변경을 하는 방법이 있나?
# ->비효율적

def solution(sizes):
    answer = 0
    low_length = []
    high_length = []
    for size in sizes:
        if size[0] <= size[1]:
            low_length.append(size[0])
            high_length.append(size[1])
        else:
            low_length.append(size[1])
            high_length.append(size[0])
    answer = max(low_length) * max(high_length)
    return answer
