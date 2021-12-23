# programmers level1 2016년
# https://programmers.co.kr/learn/courses/30/lessons/12901
# 2016년 1월 1일은 금요일
# 1월 1일부터 a월 b일이 몇 일이 경과했는지 측정
# 각 월이 몇일까지 있는지 정의 필요


def solution(a, b):
    month = {'1': 31, '2': 29, '3': 31, '4': 30, '5': 31, '6': 30,
             '7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}
    day = {'2': 'SUN', '3': 'MON', '4': 'TUE',
           '5': 'WED', '6': 'THU', '0': 'FRI', '1': 'SAT'}
    count = -1
    for i in range(1, a):
        count += month[str(i)]
    count += b
    answer = day[str(count % 7)]
    return answer


print(solution(1, 2))
