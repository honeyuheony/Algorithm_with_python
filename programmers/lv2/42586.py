# programmers level2 기능개발
# https://programmers.co.kr/learn/courses/30/lessons/42586
# 스택, 큐
# 리스트의 앞부터 검색해 100인값 순차배출 / 100이 아니면 중단

def solution(progresses, speeds):
    answer = []
    count_finish_item = 0
    while(len(progresses)):
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for p in progresses:
            if p >= 100:
                count_finish_item += 1
            else:
                break
        if count_finish_item > 0:
            answer.append(count_finish_item)
            while(count_finish_item):
                progresses.pop(0)
                speeds.pop(0)
                count_finish_item -= 1
    return answer


# Test Code
print(solution([99, 98, 97, 96, 95], [1, 1, 2, 1, 3]))
