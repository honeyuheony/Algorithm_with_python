# 탐색문제
# point :
# 문제에서 주어진 배열은 행->열 순임으로 하나의 list가 한 열을 뜻하지 않는다.
# 인형 2개가 모여 터지는 것은 말 그대로 인형 2개가 사라지는 것이다.

def solution(board, moves):
    answer = 0
    busket = []
    for move in moves:
        try:
            temp = 0
            for row in board:
                if row[move-1] != 0:
                    temp = row[move-1]
                    row[move-1] = 0
                    break
                else:
                    continue
            if temp and len(busket) and busket[len(busket)-1] == temp:
                answer += 2
                busket.pop()
            else:
                busket.append(temp)
        except:
            pass
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print(solution(board, moves))
