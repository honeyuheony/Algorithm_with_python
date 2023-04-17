# baekjoon s5 단어 정렬
# https://www.acmicpc.net/problem/1181
# 정렬, 문자열
# 글자수, 일반 두개의 key를 사용해 정렬
N = int(input())
words = list(set([input() for _ in range(N)]))
words.sort(key=lambda x : (len(x), x))
[print(w) for w in words]
    