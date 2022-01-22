# baekjoon s5 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
# 수학

import math

m, n = map(int, input().split())
print(math.gcd(m, n))
print(int(m * n / math.gcd(m, n)))
