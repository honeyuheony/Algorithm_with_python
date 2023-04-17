# baekjoon s3 피보나치 함수
# https://www.acmicpc.net/problem/1003
# 1. 0의 개수는 fibo(n-1), 1의 개수는 fibo(n)
# 2. 두 값을 동시에 구하기 위해 재귀호출이 아닌 순차계산으로 피보나치계산
import sys


def fibonacci_count(n):
    if n == 0:
        return "1 0\n"
    elif n == 1:
        return "0 1\n"
    elif n == 2:
        return "1 1\n"
    else:
        a, b = 1, 1
        for i in range(2, n):
            a, b = b, a+b
        return f"{a} {b}\n"


N = int(sys.stdin.readline())
for i in range(N):
    d = int(sys.stdin.readline())
    sys.stdout.write(fibonacci_count(d))
