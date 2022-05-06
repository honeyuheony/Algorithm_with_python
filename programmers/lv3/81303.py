# programmers level3 표 편집
# https://programmers.co.kr/learn/courses/30/lessons/81303

# stack 생성
# 삭제한 데이터는 redo를 위해 stack에 저장
# U, D 이동 및 삭제시 위치선정 구현
# - 삭제한 행이 포함된 곳을 이동할 때는? 카운트해보자
# redo시 위치 변하지 않음
# 반환은 전체원소 > stack에 있으면 X 없으면 O

from collections import deque


def solution(n, k, cmd):
    class node:
        def __init__(self, idx, up, down):
            self.idx = idx
            self.up = up
            self.down = down
            self.state = "O"

    def up(k, v):
        for i in range(v):
            k = table[k].up
        return k

    def down(k, v):
        for i in range(v):
            k = table[k].down
        return k

    def delete(k, v):
        pick = table[k]
        pick.state = "X"
        deleted.appendleft(pick)
        if pick.up != None:
            table[pick.up].down = pick.down
        if pick.down != None:
            table[pick.down].up = pick.up
        return pick.down if pick.down != None else pick.up

    def redo(k, v):
        pick = deleted.popleft()
        pick.state = "O"
        if pick.up != None:
            table[pick.up].down = pick.idx
        if pick.down != None:
            table[pick.down].up = pick.idx
        return k

    deleted = deque()
    table = [node(i, i-1, i+1) for i in range(n)]
    table[0].up = None
    table[n-1].down = None
    method_mapping = {"D": down, "U": up, "C": delete, "Z": redo}
    for c in cmd:
        a = int(c[2:]) if len(c) != 1 else 0
        k = method_mapping[c[0]](k, a)

    return ''.join([t.state for t in table])


# TEST
n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))
