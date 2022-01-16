# baekjoon s5 영화감독 숌
# https://www.acmicpc.net/problem/1436
# 브루트포스

n = int(input())
solve = []
i = 1
while len(solve) < n:
    if '666' in str(i):
        solve.append(i)
    i += 1
solve.reverse()
print(solve[0])