def solution(new_id):
    able = ['-', '_', '.']
    new_id = new_id.lower()
    for n in new_id:
        if n.isalpha() or n.isdigit() or n in able:
            print(n, n.isalpha(), n.isdigit(), n in able)
        else:
            new_id = new_id.replace(n, '')

    is_dot = False
    for n in new_id:
        if n == '.' and is_dot:
            pass
        elif n == '.':
            is_dot = True
        else:
            is_dot = False
    answer = ''
    return answer


solution('...!@BaT#*..y.abcdefghijklm')
