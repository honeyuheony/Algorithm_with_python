# baekjoon b2 벌집
# https://www.acmicpc.net/problem/2292
# 벌집 층별 칸 개수 : 2*(1 + 2k) + (k-1)
N = int(input())
N -=1
f = 1
room = 1
while room < N+1:
    room += 2*(1 + 2*f) + 2*(f-1)
    f += 1
print(f)