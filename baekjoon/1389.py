# baekjoon s2 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389
# 1. 1 ~ M 의 수를 시작점으로 하는 BFS M번 수행
# 2. 각 BFS에서 새로운 곳에 도달할때의 탐색 횟수 기록해 합 구하기
# 3. 합이 가장 작은 index + 1 출력

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
graph = {}
for i in range(1, M+1):
    graph[i] = []
for i in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, M+1):
    bacon_num = 0
    count = 1
    queue, visited, temp = [], [], []
    queue.append(i)
    visited.append(i)
    while True:
        q = queue.pop(0)
        for j in graph[q]:
            if not j in visited:
                visited.append(j)
                temp.append(j)
                bacon_num += count
        if len(queue) == 0:
            queue = temp
            temp = []
            count += 1
            if len(visited) == M:
                break
    result.append(bacon_num)
print(result.index(min(result))+1)
