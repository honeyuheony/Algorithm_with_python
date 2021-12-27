# programmers level1 시저암호
# https://programmers.co.kr/learn/courses/30/lessons/12926
# ascii -> chr((ord(i) + n - 65) % 26 + 65)

def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            answer += chr((ord(i) + n - 65) % 26 + 65)
        elif i.islower():
            answer += chr((ord(i) + n - 97) % 26 + 97)
        else:
            answer += ' '
    return answer


print(solution("ab", 3))
