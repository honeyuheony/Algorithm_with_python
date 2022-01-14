# baekjoon s5 단어 정렬
# https://www.acmicpc.net/problem/1181
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 
# 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
N = int(input())
words = list(set([input() for _ in range(N)]))
words.sort(key=lambda x : (len(x), x))
[print(w) for w in words]
    