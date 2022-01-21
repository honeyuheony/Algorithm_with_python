# baekjoon b2 분해합
# https://www.acmicpc.net/problem/2231

N = int(input())
result = 0
for i in range(1, N+1):
    s = sum([int(a) for a in str(i)])
    if i == N-s:
        result = i
        break
print(result)