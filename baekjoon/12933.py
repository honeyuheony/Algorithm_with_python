import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

quack_order_map = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}
quack_count_list = [0, 0, 0, 0, 0]


def solution(str):
    for s in str:
        if check_and_count_quack(s) == False:
            return -1
    if sum(quack_count_list[:4]) > 0:
        return -1
    return sum(quack_count_list)


def check_and_count_quack(s):
    pre_index = quack_order_map.get(s, 0) - 1
    if s != 'q':
        if quack_count_list[pre_index] == 0:
            return False
        else:
            quack_count_list[pre_index + 1] += 1
            quack_count_list[pre_index] -= 1
    else:
        quack_count_list[0] += 1
        if quack_count_list[4] != 0:
            quack_count_list[4] -= 1
    return True


sound = input().strip()
print(solution(sound))


"""
알파벳을 검사해서 해당 알파벳 순서가 올 수 없는 경우(앞의 울음이 없다) -> -1 반환
알파벳이 q라면 그냥 값 추가 아니라면 
"""
