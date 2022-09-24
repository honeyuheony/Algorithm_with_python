'''
programmers level1 신고 결과 받기
https://programmers.co.kr/learn/courses/30/lessons/87389
'''


def solution(id_list, report, k):
    report_dict = {i: set() for i in id_list}
    answer_dict = {i: 0 for i in id_list}
    for r in report:
        a, b = r.split()
        report_dict[b].add(a)
    for i in id_list:
        if len(report_dict[i]) >= k:
            for id in report_dict[i]:
                answer_dict[id] += 1
    return [answer_dict[i] for i in id_list]


print(solution(["muzi", "frodo", "apeach", "neo"], [
      "muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
