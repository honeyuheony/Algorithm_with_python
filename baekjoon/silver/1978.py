# baekjoon s4 소수 찾기
# https://www.acmicpc.net/problem/1978
# 정수론
import math

N = int(input())
num_list = list(map(int, input().split()))
result = 0
if 1 in num_list:
    num_list.remove(1)
if 2 in num_list:
    num_list.remove(2)
    result += 1
if 3 in num_list:
    num_list.remove(3)
    result += 1

for n in num_list:
    for i in range(2, math.ceil(math.sqrt(n)+1)):
        if n % i == 0:
            break
        if i == math.ceil(math.sqrt(n)):   
            result += 1

print(result)