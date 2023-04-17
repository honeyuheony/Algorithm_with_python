# baekjoon s5 덩치
# https://www.acmicpc.net/problem/7568
# 1. 자기보다 몸무게도 더 높고 키도 더 높은 사람 세기
import sys

N = int(sys.stdin.readline())
people = []
for i in range(N):
    x, y, = map(int, sys.stdin.readline().split())
    people.append({'weight': x, 'height': y, 'index': i})
# people.sort(key = lambda x : (x['height'], x['weight']), reverse=True)
# print(people)

for p in people:
    height = p['height']
    weight = p['weight']
    p['rank'] = len([e for e in people if e['height'] > height and e['weight'] > weight])
print(' '.join([str(p['rank']+1) for p in people]))