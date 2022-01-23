# baekjoon b3 ACM호텔
# https://www.acmicpc.net/problem/10250
# 수학
# 1. k번째 손님이 묶는 층 번호 : str(k % h) if k % h else str(h)
# 2. 방 번호 : '%02d' %(((k-1) // h)+1)
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    h, w, k = map(int, sys.stdin.readline().split())
    floor = str(k % h) if k % h else str(h)
    num = '%02d' %(((k-1) // h)+1)
    print(floor + str(num))