# programmers level1 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

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
