# programmers level1 이상한 문자 만들기
# https://programmers.co.kr/learn/courses/30/lessons/12930
# 공백을 기준으로 나눈 문자열들을 짝수번째 인덱스 upper, 홀수번째 인덱스 lower
# str은 인덱스수정이어려움


def solution(s):
    s = s.split(' ')
    answer = []
    for word in s:
        temp = ''
        for index, w in enumerate(word):
            if index % 2 == 0:
                temp += w.upper()
            else:
                temp += w.lower()

        answer.append(temp)
    return ' '.join(answer)


print(solution('try hello world'))
