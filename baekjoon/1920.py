# baekjoon s4 수 찾기
# https://www.acmicpc.net/problem/1920
# 집합
# 1. 둘의 교집합과 비교한다.

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

result = set(B) - set(A)
for b in B:
    print("0") if b in result else print("1")

    
