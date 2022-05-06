# programmers level2 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302

# 1. 각 대기자의 멘해튼거리 확인
# 2. 멘해튼거리가 2 이하라면 파티션 확인
#   2-1. 거리가 1이라면 거리두기 X
#   2-2. 거리가 2이고 직선배치인 경우 -> 직선거리 파티션 하나라도 있는지 확인
#   2-3. 거리가 2이고 대각배치인 경우 -> 대각 방향 2가지 경우 파티션 검사
def solution(places):
    answer = []
    for place in places:
        people = []
        for index, p in enumerate(place):
            for i in range(5):
                if p[i] == 'P':
                    people.append((index, i))
        flag = True
        while flag and people:
            person = people.pop(0)
            for p in people:
                distance = abs(person[0] - p[0]) + \
                    abs(person[1] - p[1])  # 멘해튼거리
                if distance == 1:
                    flag = False
                    break
                elif distance == 2:
                    if abs(person[0] - p[0]) == 2:  # 거리가 가로직선인 경우
                        if not place[min(p[0], person[0])+1][p[1]] == 'X':
                            flag = False
                            break
                    elif abs(person[1] - p[1]) == 2:  # 거리가 세로직선인 경우
                        if not place[p[0]][min(p[1], person[1])+1] == 'X':
                            flag = False
                            break
                    else:  # 거리가 대각선인 경우
                        side = []
                        if person[0] > p[0]:
                            side.append(place[person[0]-1][person[1]])
                        else:
                            side.append(place[person[0]+1][person[1]])
                        if person[1] > p[1]:
                            side.append(place[person[0]][person[1]-1])
                        else:
                            side.append(place[person[0]][person[1]+1])
                        for s in side:
                            if s != 'X':
                                flag = False
                                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer
