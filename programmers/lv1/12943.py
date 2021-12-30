# programmers level1 콜라즈추측
# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0
    while(num != 1 and count < 500):
        if not num % 2:
            num /= 2
        else:
            num = num * 3 + 1
        count += 1
    return count if count < 500 else -1
