# programmers level1 핸드폰 번호 가리기
# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    return ''.join(['*' for _ in range(len(phone_number)-4)]) + phone_number[len(phone_number)-4:len(phone_number)]


print(solution('01050056246'))
