# programmes level2 행렬태두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485
# Stack, 구현
# 시계방향 회전하는 칸의 개수: row * col - (row-2) * (col-2)
# 회전할 칸 내부 값을 리스트에 담아 한칸씩 이동 후 다시 회전칸 채우기
# 회전칸 = [r1c1 ~ r1c2 and r1c2 ~ r2c2 and r2c2 ~ r2c1 and r2c1 ~ r1c1]
from queue import deque


def solution(rows, columns, queries):
    matrix = [[c+r*columns for c in range(1, columns+1)]
              for r in range(rows)]
    answer = []
    for q in queries:
        point = deque()
        r1, c1, r2, c2 = q
        for i in range(c1, c2):
            point.append((matrix[r1-1][i-1]))
        for i in range(r1, r2):
            point.append((matrix[i-1][c2-1]))
        for i in range(c2, c1, -1):
            point.append((matrix[r2-1][i-1]))
        for i in range(r2, r1, -1):
            point.append((matrix[i-1][c1-1]))
        point.appendleft(point.pop())
        answer.append(min(point))
        for i in range(c1, c2):
            matrix[r1-1][i-1] = point.popleft()
        for i in range(r1, r2):
            matrix[i-1][c2-1] = point.popleft()
        for i in range(c2, c1, -1):
            matrix[r2-1][i-1] = point.popleft()
        for i in range(r2, r1, -1):
            matrix[i-1][c1-1] = point.popleft()
    return answer


# Test Code
print(solution(3, 4, [[1, 1, 3, 2], [1, 2, 3, 3], [1, 3, 3, 4]]))
