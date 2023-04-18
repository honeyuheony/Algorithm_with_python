# baekjoon s1 타이핑
# https://www.acmicpc.net/problem/25215

import sys
input = sys.stdin.readline

string = input().strip()
is_upper_char_list = []

for s in string:
    is_upper_char_list.append(s.isupper())

part_of_str_list = []
part_of_str = [is_upper_char_list[0], 1]

for s in is_upper_char_list[1:]:
    if part_of_str[0] == s:
        part_of_str[1] += 1
    else:
        part_of_str_list.append(part_of_str)
        part_of_str = [s, 1]
part_of_str_list.append(part_of_str)

current_type = False
result = 0

for i in range(0, len(part_of_str_list)):
    result += part_of_str_list[i][1]
    if part_of_str_list[i][0] != current_type:
        if part_of_str_list[i][1] != 1:
            current_type = not current_type
        result += 1

print(result)
