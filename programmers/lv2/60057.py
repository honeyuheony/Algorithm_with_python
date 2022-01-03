# programmers level2 문자열압축
# https://programmers.co.kr/learn/courses/30/lessons/60057
# 문자열의 반복패턴을 찾아 가장 짧게 압축할 수 있는 길이 반환
# 문자열, 구현
# 1 ~ 문자열 절반길이까지 슬라이싱 후 자른 토막끼리 연속검사
# 압축문자열 생성하고 길이검사

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        zip_str = ''
        count = 1
        for j in range(0, (len(s)//i)):
            if s[i*j:i*(j+1)] == s[i*(j+1):i*(j+2)]:
                count += 1
            else:
                if count > 1:
                    zip_str += str(count) + s[i*j:i*(j+1)]
                else:
                    zip_str += s[i*j:i*(j+1)]
                count = 1
        if len(s) % i != 0:
            zip_str += s[len(s)-(len(s) % i):]
        if len(zip_str) < answer:
            answer = len(zip_str)
    return answer


# Test code
print(solution('aabbaccc'))
