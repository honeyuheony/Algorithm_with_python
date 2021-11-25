def solution(lottos, win_nums):
    match = 0
    zero_cnt = 0
    for l in lottos:
        if l == 0:
            zero_cnt += 1
        elif l in win_nums:
            match += 1

    low_rank = 7 - match if match >= 2 else 6
    high_rank = 7 - (match + zero_cnt) if match + zero_cnt >= 2 else 6
    answer = [high_rank, low_rank]
    return answer


lottos = []
win_nums = []
print(solution(lottos, win_nums))
