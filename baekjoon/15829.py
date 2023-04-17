# baekjoon b2 해쉬
# https://www.acmicpc.net/problem/15829

import sys

N = int(sys.stdin.readline())
s = list(sys.stdin.readline().split('\n')[0])
result = 0
for index, i in enumerate(s):
    result += (int(ord(i)) - 96) * pow(31, index)
sys.stdout.write(str(result % 1234567891) + '\n')
