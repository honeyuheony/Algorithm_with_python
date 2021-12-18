def solution(absolutes, signs):
    answer = 123456789
    answer_list = [absolutes[i] if signs[i] else -absolutes[i]
                   for i, n in enumerate(signs)]
    answer = sum(answer_list)
    return answer


absolutes = [4, 7, 12]
signs = [True, False, True]
print(solution(absolutes, signs))
