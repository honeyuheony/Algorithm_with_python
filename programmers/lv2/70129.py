'''
programmers level2 이진 변환 반복하기
https://school.programmers.co.kr/learn/courses/30/lessons/70129
'''


def solution(s):
    answer = [0, 0]
    while s != '1':
        prev_length = len(s)
        s = s.replace('0', '')
        curr_length = len(s)
        s = format(len(s), 'b')
        answer[1] += prev_length - curr_length
        answer[0] += 1

    return answer


print(solution("110010101001"))
