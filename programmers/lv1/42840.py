# programmers level1 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

# 완전탐색

def solution(answers):
    answer = []
    count = {'1': 0, '2': 0, '3': 0}
    type_one = [1, 2, 3, 4, 5]
    type_two = [2, 1, 2, 3, 2, 4, 2, 5]
    type_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for index, a in enumerate(answers):
        if a == type_one[index % len(type_one)]:
            count['1'] += 1
        if a == type_two[index % len(type_two)]:
            count['2'] += 1
        if a == type_three[index % len(type_three)]:
            count['3'] += 1

    for key, value in count.items():
        if value == max(count.values()):
            answer.append(int(key))
    return answer
