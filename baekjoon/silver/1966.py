# baekjoon s3 프린터 큐
# https://www.acmicpc.net/problem/1966
# 우선순위큐
# 1. 큐에 (우선순위, 인덱스) 튜플 삽입
# 2. get 후 우선순위가 가장 높지 않다면 다시 put
# 3. 우선순위가 높다면 인덱스 검사
from queue import Queue

N = int(input())
for _ in range(N):
    length, index = map(int, input().split())
    priority = list(map(int, input().split()))
    docs = Queue()
    for i, p in enumerate(priority):
        docs.put((p, i))
    result = 0
    while True:
        temp = docs.get()
        if temp[0] == max(priority):
            result += 1
            priority.remove(temp[0])
            if temp[1] == index:
                print(result)
                break
        else:
            docs.put(temp)
        
            
