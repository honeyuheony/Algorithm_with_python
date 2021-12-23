# programmers level1 나머지가 1이 되는 수 찾기
# https://programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    answer = 1
    while(True):
        if n % answer == 1:
            return answer
        else:
            answer += 1
