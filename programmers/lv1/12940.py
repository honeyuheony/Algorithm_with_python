# programmers level1 최대공약수와 촤소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최소공배수 : 최대공약수 * a의 남은 값 * b의 남은 값
# 최대공약수 : 공통약수
def solution(n, m):
    if m < n:
        n, m = m, n
    n_divisor = []
    for i in range(1, n//2 + 1):
        if not n % i:
            n_divisor.append(i)
    n_divisor.append(n)
    m_divisor = []
    for i in range(1, m//2 + 1):
        if not m % i:
            m_divisor.append(i)
    m_divisor.append(m)
    max_divisor = max(set(n_divisor) & set(m_divisor))
    min_multiple = (n / max_divisor) * m
    return [max_divisor, min_multiple]


print(solution(3, 12))
