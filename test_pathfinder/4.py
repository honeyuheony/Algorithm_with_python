#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reachTheEnd' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER maxTime
#
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def reachTheEnd(grid, maxTime):

    if len(grid) == 1 and len(grid[0]) == 1:
        return 'Yes'

    x = y = t = 0
    q = deque()
    q.append((y, x))
    visited = []
    used_time = []
    for i in grid:
        u = []
        for j in i:
            u.append(0)
        used_time.append(u)

    while(len(q) > 0):
        current_place = q.popleft()
        x = current_place[1]
        y = current_place[0]

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_y][next_x] != '#':
                if not used_time[next_y][next_x]:
                    q.append((next_y, next_x))
                    used_time[next_y][next_x] = used_time[y][x] + 1
    if used_time[len(grid)-1][len(grid[0])-1] != 0:
        if used_time[len(grid)-1][len(grid[0])-1] <= maxTime:
            return "Yes"
        else:
            return "No"
    else:
        return "No"


if __name__ == '__main__':
