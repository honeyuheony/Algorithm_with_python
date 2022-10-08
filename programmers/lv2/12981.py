'''
programmers level2 영어 끝말잇기
https://school.programmers.co.kr/learn/courses/30/lessons/12981
'''

def solution(n, words):
    used_word = set([words[0]])
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in used_word:
            loser = (i+1) % n if (i+1) % n != 0 else n
            turn = i // n + 1
            return [loser, turn]
        used_word.add(words[i])
    # 패배자 없음
    return [0, 0]