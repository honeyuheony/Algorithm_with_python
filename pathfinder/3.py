#!/bin/python3

import math
import os
import random
import re
import sys
import random


#
# Complete the 'segment' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER_ARRAY space
#

def segment(x, space):
    result = 0
    segments = []
    for i in range(0, len(space)-x+1):
        segments.append(space[i:i+x])
    print(segments)
    for s in segments:
        if result < min(s):
            result = min(s)
    return result
    # Write your code here


space = []
for i in range(1000000):
    space.append(random.randint(1, 2))

print(segment(10000, space))
