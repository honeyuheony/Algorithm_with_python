# programmers level1 수박
# https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    s = ['수', '박']
    answer = ''.join([s[i % 2] for i in range(n)])
    return answer


print(solution(4))
