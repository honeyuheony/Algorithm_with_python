# baekjoon s5 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609
# 수학, 정수론
# 최소공배수 : 두 수를 곱한 뒤 최대공약수로 나눈 값

import math

m, n = map(int, input().split())
print(math.gcd(m, n))
print(int(m * n / math.gcd(m, n)))
