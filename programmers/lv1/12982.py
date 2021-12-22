# programmers level1 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982
# d : 지원요청금액이 담긴 배열
# budget : 총 예산 금액
# 탐욕적 접근을 통한 해결
# 지원가능한 부서의 최대값을 구하는 문제이므로 가격의 오름차순으로 정렬
# 정렬된 리스트를 순차계산후 더이상 예산 사용 불가시 종료

# def solution(d, budget):
#     answer = 0
#     d.sort()
#     for i in d:
#         budget -= i
#         if budget >= 0:
#             answer += 1
#         else:
#             break
#     return answer

# 연산량을 줄이기 위해 할 수 있는 것
# 부서당 필요 예산액의 평균을 구해서 총 예산액 / 평균으로 예상 answer을 유추한 후 증감연산 진행


def solution(d, budget):
    answer = 0
    d.sort()
    middle = sum(d) / len(d)
    answer = int(budget // middle)
    if answer > len(d):
        answer = len(d)
    if sum(d[0:answer]) > budget:
        d = d[0:answer]
        while(sum(d) <= budget):
            d.pop()
            answer -= 1
    elif sum(d[0:answer]) < budget:
        budget -= sum(d[0:answer])
        while(budget >= d[answer-1] and answer < len(d)):
            budget -= d[answer-1]
            answer += 1
    return answer


print(solution([1, 3, 2, 5, 4], 9))
