# programmers level1 부족한 돈 채우기
# https://programmers.co.kr/learn/courses/30/lessons/82612
# n회 놀이기구 탑승 금액은 price * factorial(n)
import math


def solution(price, money, count):
    return 0 if money >= price * (count * (count+1)) / 2 else abs(money - price * (count * (count+1)) / 2)
