# programmers level2 더 맵게
# https://programmers.co.kr/learn/courses/30/lessons/42626
# 최소Heap 연산 수행
# 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(scoville[0] < K and len(scoville) > 1):
        heapq.heappush(scoville, heapq.heappop(
            scoville) + 2 * heapq.heappop(scoville))
        answer += 1
    return answer if scoville[0] >= K else -1


print(solution([1, 2], 7))
