'''
programmers level2 캐시
https://school.programmers.co.kr/learn/courses/30/lessons/17680
'''
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    cache_q = deque(maxlen=cacheSize)
    for city in cities:
        city = city.upper()
        if city in cache_q:  # cache hit
            cache_q.remove(city)
            answer += 1
        else:  # cache miss
            answer += 5
        cache_q.append(city)

    return answer
t = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(solution(0, t))
