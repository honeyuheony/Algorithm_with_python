
#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


#
# Complete the 'countSubstrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING input_str as parameter.
#

mapped_alphabet = {'a': 1, 'b': 1, 'c': 2, 'd': 2, 'e': 2, 'f': 3, 'g': 3, 'h': 3, 'i': 4, 'j': 4, 'k': 4, 'l': 5,
                   'm': 5, 'n': 5, 'o': 6, 'p': 6, 'q': 6, 'r': 7, 's': 7, 't': 7, 'u': 8, 'v': 8, 'w': 8, 'x': 9, 'y': 9, 'z': 9}


def countSubstrings(input_str):
    tmp = ''
    for i in range(len(input_str)):
        tmp += str(mapped_alphabet[input_str[i]])
    input_str = tmp
    result = 0
    combination = []
    for i in range(0, len(input_str)):
        for j in range(i+1, len(input_str)+1):
            combination.append(input_str[i:j])
    for string in combination:
        str_sum = 0
        for s in string:
            str_sum += int(s)
        if not str_sum % len(string):
            result += 1
    return result


print(countSubstrings('asdf'))
