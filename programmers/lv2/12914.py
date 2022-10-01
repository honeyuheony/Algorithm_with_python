'''
programmers level2 멀리 뛰기
https://school.programmers.co.kr/learn/courses/30/lessons/12914
2 -> 2 (1 1) (2)
3 -> 3 (2 1) (1 2) (1 1 1)
4 -> 5 (1 1 2) (2 2) (2 1 1) (1 2 1) (1 1 1 1)
5 -> 8 (3 + 5)
'''


def solution(n):
    dp = [0, 1, 2] + [0 for _ in range(3, n+1)]
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567


print(solution(4))
