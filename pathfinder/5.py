#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

#
# Complete the 'minimumDivision' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#  3. INTEGER k
#


def minimumDivision(a, b, k):
    division_list = []
    for i in range(len(a)):
        division_list.append((a[i], b[i]))
    division_list.sort()
    result_division = []

    division = 1
    for i in range(len(division_list)-1):
        if division_list[i][1] < division_list[i+1][0]:
            division += 1
            result_division.append(
                (division_list[i][1], division_list[i+1][0]))

    for i in result_division:
        if i[1] - i[0] <= k:
            if division == 1:
                return division
            return division - 1
    return division

    # for i in range(len(a)):
    #     for j in range(a[i], b[i]+1):
    #         division_list.append(j)
    # print(set(division_list))


a = [6, 2, 13, 27, 45, 45, 33]
b = [6, 10, 24, 40, 45, 45, 33]
k = 12
print(minimumDivision(a, b, k))
