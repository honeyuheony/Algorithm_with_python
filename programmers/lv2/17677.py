# programmers level2 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    '''
    1. str1, str2의 다중집합 원소 딕셔너리 만들기
    2. 더 작은 길이의 딕셔너리의 key를 하나씩 꺼내 더 큰 길이의 딕셔너리에 동일한 key가 있는지     검사, 값도 검사
    3. 검사해 다중집합의 교집합 생성, A + B - 교집합으로 합집합 크기 구해서 자카드 유사도 계산
    '''
    def create_multiset(str):
        str = str.lower()
        multiset = {}
        used = set()
        for i in range(len(str)-1):
            e = str[i:i+2]
            if not e.isalpha():
                continue
            elif e in used:
                multiset[e] += 1
            else:
                used.add(e)
                multiset[e] = 1
        return multiset
    
    multiset_str1 = create_multiset(str1)
    multiset_str2 = create_multiset(str2)
    
    def get_intersection_size(small_set, big_set):
        result = 0
        for key in small_set.keys():
            if big_set.get(key, None):
                result += min(small_set[key], big_set[key])
        return result
    
    intersection_size = 0
    if len(multiset_str1) < len(multiset_str2):
        intersection_size = get_intersection_size(multiset_str1, multiset_str2)
    else:
        intersection_size = get_intersection_size(multiset_str2, multiset_str1)
    
    combined_size = sum(multiset_str1.values()) + sum(multiset_str2.values()) - intersection_size
    result = 1 if combined_size == 0 else intersection_size / combined_size
    return int(result * 65536)

print(solution('handshake', 'shake hands'))