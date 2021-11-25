#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests


def getTopRatedFoodOutlets(city):
    url = 'https://jsonmock.hackerrank.com/api/food_outlets?'
    body = f'city={city}&page='
    init = 1
    result_score = 0
    result_name = []
    res = requests.get(url + body + str(init))
    for r in range(int(res.json()['total_pages'])):
        res = requests.get(url + body + str(r+1))
        for i in res.json()['data']:
            if result_score < i['user_rating']['average_rating']:
                result_score = i['user_rating']['average_rating']
                result_name = [i['name']]
            elif result_score == i['user_rating']['average_rating']:
                result_name.append(i['name'])
    return result_name


city = 'Denver'
print(getTopRatedFoodOutlets(city))
