# baekjoon s2 소수 구하기
# https://www.acmicpc.net/problem/1929
# 1. 1 ~ sqrt(N)의 수로 나눠지지 않는 N은 소수
# 2. 연산량을 줄이기 위해 1 ~ sqrt(N) 중의 소수 구하기
import math

M, N = map(int, input().split())
if M == 1:
    M = 2
prime = [2, 3]
temp = int(math.sqrt(N))+1
for i in range(4, temp):
    for d in range(2, int(math.sqrt(temp))+1):
        if i % d == 0 :
            break
        if d == int(math.sqrt(i)):
            prime.append(i)
result = []
for i in range(M, N+1):
    if i in prime:
        result.append(i)
        continue
    for d in prime:
        if i % d == 0:
            break
        if d == prime[len(prime)-1]:
            result.append(i)
for r in result:
    print(r)