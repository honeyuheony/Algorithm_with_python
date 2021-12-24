# programmers level1 같은 숫자는 싫어
# https://programmers.co.kr/learn/courses/30/lessons/12906
# 전 값과 같다면 다르다면 새 배열에 담기
def solution(arr):
    answer = []
    last = -1
    for a in arr:
        if a != last:
            answer.append(a)
        last = a
    return answer


print(solution([4, 4, 3, 3, 3]))
