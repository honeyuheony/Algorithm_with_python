import math
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    threshold = M*N / math.gcd(M, N)
    isValidMonth = False
    year = x if M > N else y
    temp = max(M, N)
    while year <= threshold:
        if year % M in (0, x) and year % N in (0, y):
            isValidMonth = True
            break
        else:
            year += temp
    if isValidMonth:
        print(year)
    else:
        print(-1)
