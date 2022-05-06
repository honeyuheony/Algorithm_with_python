# programmers level2 괄호변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

# 1. 순차검사로 균형잡힌 문자열 하나 찾기
# 2. 찾으면 그 문자열과 뒤 문자열 두개로 나누기
# 3. 앞 문자열이 올바른 문자열인지 검사 -> 수행
# 4. 뒷 문자열에서 1번부터 수행

# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

def solution(p):
    answer = ''
    # 1번 알고리즘 숳행
    if len(p) == 0:
        return answer
    left, right = 0, 0
    complete = True
    # 2번 알고리즘 수행
    for index, c in enumerate(p):
        if c == '(':
            left += 1
        else:
            right += 1
        if left < right:
            complete = False
        if left == right:  # 균형잡힌 문자열 찾음
            if complete:  # 올바른 문자열이라면 -> 3번 알고리즘 수행
                answer += p[0:index+1]
                if len(p[index+1:]) != 0:  # v문자열이 빈 문자열이 아니라면
                    answer += solution(p[index+1:])
            else:  # 4번 알고리즘 수행
                answer = answer + '(' + solution(p[index+1:]) + ')'
                for c in p[1:index]:
                    if c == '(':
                        answer += ')'
                    else:
                        answer += '('
            return answer


# Test
print(solution('))(()('))
