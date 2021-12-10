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
            print(temp)
            if temp and len(busket) and busket[len(busket)-1] == temp:
                print(temp)
                print('')
                answer += 1
                busket.pop()
            else:
                busket.append(temp)
        except:
            pass
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
print('')
print(solution(board, moves))
