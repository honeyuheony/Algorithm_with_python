# programmers level1 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

# 해싱과 유사한 기법을 사용
# 문자열의 길이와 첫글자를 토대로 입력값 분류해 탐색을 효과적으로 만듦.
# 해싱을 이용한다면 더 좋은 해결 가능
def solution(participant, completion):

    hash_completion = [[[] for col in range(20)] for row in range(26)]
    answer = ''
    for c in completion:
        hash_completion[ord(c[0])-97][len(c)-1].append(c)
    for p in participant:
        if p in hash_completion[ord(p[0])-97][len(p)-1]:
            hash_completion[ord(p[0])-97][len(p)-1].remove(p)
            continue
        else:
            answer = p
    return answer
