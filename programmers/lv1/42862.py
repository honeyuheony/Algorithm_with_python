# programmers level1 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    temp = list(set(lost) - set(reserve))
    reserve = list(set(reserve) - set(lost))
    lost = temp

    lost.sort()
    reserve.sort()
    answer = n - len(lost)

    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
            answer += 1
        elif l+1 in reserve:
            reserve.remove(l+1)
            answer += 1
    return answer
