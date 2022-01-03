# programmers level2 오픈채팅방
# https://programmers.co.kr/learn/courses/30/lessons/42888
# 문자열, 구현
# uid에 해당하는 nickname값은 최신 값만 반영하면 된다.
# 1. uid : nickname 형태의 딕셔너리 생성 (record의 마지막값까지 반영)
# 2. nickname 님이 ㅇㅇ했습니다 형태의 출력 리스트 구현
def solution(record):
    uid_dict = {}
    type_dict = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}
    for r in record:
        words = r.split()
        if words[0] != 'Leave':
            uid_dict[words[1]] = words[2]
    answer = []
    for r in record:
        words = r.split()
        if words[0] != 'Change':
            answer.append(uid_dict[words[1]] + type_dict[words[0]])
    return answer


# Test Code
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
          "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(solution(record))
