# baekjoon s3 나무자르기
# https://www.acmicpc.net/problem/2805
# 이진탐색

import sys
M, H = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(trees)-1
while end - start > 1:
    mid = (start + end) // 2
    if sum([tree - mid for tree in trees if tree > mid]) >= H:
        start = mid
    else:
        end = mid - 1
if sum([tree - end for tree in trees if tree > end]) >= H:
    print(end)
else:
    print(start)