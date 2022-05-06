from collections import deque

# 트리


# BFS
# 1. 너비우선으로 탐색하기 위해 다음 방문할 노드를 queue에 삽입
# 2. 중간 단계를 기록해야하는 경우 temp 사용해 한번 빠져나온 뒤 다시 queue 생성

# DFS
# 1. 깊이 우선으로 탐색하기 위해 다음 방문핧 노드를 stack에 삽입
# 2. 보통 재귀로 구현

# DP

# Greedy

# 브루트포스

# 백트래킹

# 이분탐색
# 1. start = 0, end = 길이-1
# 2. mid = (start + end) // 2
# 3-1. mid값이 target보다 작다면 end = mid-1
# 3-2. mid값이 target보다 크다면 start = mid + 1
