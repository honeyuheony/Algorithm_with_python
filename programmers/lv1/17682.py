# programmers level1 다트게임
# https://programmers.co.kr/learn/courses/30/lessons/17682
# 정규식 통한 점수 문자열 분할
import re
import math


def solution(dartResult):
    mag = {'S': 1, 'D': 2, 'T': 3}
    option = []
    scores = []
    p = re.compile('[0-9]+[SDT]?[*#]?')
    string = p.findall(dartResult)
    for s in string:
        num = re.compile('[0-9]+').findall(s)[0]
        scores.append(int(math.pow(int(num), mag[s[len(num)]])))
        if len(s) - len(num) == 2:
            option.append(s[len(s) - len(num)])
        else:
            option.append(' ')
    for index, o in enumerate(option):
        if o == '*':
            scores[index] *= 2
            print(index)
            if index != 0:
                scores[index-1] *= 2
        elif o == '#':
            scores[index] = -scores[index]
    return sum(scores)


print(solution('1S2D*3T'))
