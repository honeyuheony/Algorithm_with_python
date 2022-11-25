'''
programmers level2 H-index
https://school.programmers.co.kr/learn/courses/30/lessons/42747
'''

def binary_search(citations):
    start = min(citations)
    end = max(citations)
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        case = [c for c in citations if c >= mid]
        if len(case) < mid:
            end = mid - 1
            continue
        elif len(case) >= mid:
            ans = max(ans, mid)
            start = mid + 1
    return ans


def solution(citations):
    citations.sort()
    return binary_search(citations)