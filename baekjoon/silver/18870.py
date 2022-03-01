# baekjoon s2 좌표압축
# https://www.acmicpc.net/problem/18870

from collections import deque
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
zip_x = {}
for index, z in enumerate(sorted(set(x))):
    zip_x[z] = index
result = [str(zip_x[i]) for i in x]
print(' '.join(result))
