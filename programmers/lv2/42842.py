'''
programmers level2 카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    yellow_sero = 0
    while True:
        yellow_sero += 1
        yellow_garo = yellow // yellow_sero
        garo, sero = yellow_garo + 2, yellow_sero + 2
        if yellow_garo * yellow_sero == yellow and 2*(garo + sero) - 4 == brown:
            return [garo, sero]