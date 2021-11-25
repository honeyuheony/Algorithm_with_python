#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests


def getTotalGoals(team, year):
    goal = 0
    # Write your code here
    url = 'https://jsonmock.hackerrank.com/api/football_matches?'
    body1 = f'year={year}&team1={team}&page='
    body2 = f'year={year}&team2={team}&page='
    init = 1
    res = requests.get(url + body1 + str(init))
    for r in range(int(res.json()['total_pages'])):
        res = requests.get(url + body1 + str(r+1))
        for i in res.json()['data']:
            goal += int(i['team1goals'])
        res = requests.get(url + body2 + str(r+1))
        for i in res.json()['data']:
            goal += int(i['team2goals'])
    return goal


if __name__ == '__main__':
