def solution(new_id):
    able = ['-', '_', '.']
    # 소문자 치환
    new_id = new_id.lower()
    # 특수문자 제거
    for n in new_id:
        if n.isalpha() or n.isdigit() or n in able:
            pass
        else:
            new_id = new_id.replace(n, '')
    # 두 개 이상의 dot 연속 제거
    while('..' in new_id):
        new_id = new_id.replace('..', '.')
    # 처음과 끝의 dot 제거
    try:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[len(new_id)-1] == '.':
            new_id = new_id[:len(new_id)-1]
    except:
        # 빈문자라면 a 대입
        if not len(new_id):
            new_id = 'a'
    # 16자 이상이라면 15자로 축소
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[len(new_id)-1] == '.':
            new_id = new_id[:len(new_id)-1]
    # 2자 이하라면 늘이기
    if len(new_id) < 3:
        while(len(new_id) < 3):
            new_id += new_id[len(new_id)-1]
    answer = new_id
    return answer


solution('abcdefghijklmn.p')


# 문자열 처리에 정규식을 이용할 수 있는지 확인
# import re
