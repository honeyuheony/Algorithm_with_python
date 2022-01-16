# baekjoon s3 랜선자르기
# https://www.acmicpc.net/problem/1654
# 이진탐색

K, N = map(int, input().split())
cable = []
for _ in range(K):
    cable.append(int(input()))
start, end = 1, max(cable)
while start <= end:
    middle = (start + end) // 2
    count = 0
    for c in cable:
        count += c // middle
    if count >= N:
        start = middle + 1
    else:
        end = middle - 1
print(end)