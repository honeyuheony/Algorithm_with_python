# baekjoon s4 통계학
# https://www.acmicpc.net/problem/2108
# 빠른 연산을 위해 사전처리하기
import sys

N = int(sys.stdin.readline())
num_list = []
num_cnt = {}
for i in range(N):
    n = int(sys.stdin.readline())
    num_list.append(n)
    try:
        num_cnt[n] += 1
    except:
        num_cnt[n] = 1
num_list.sort()
commom_count = max(num_cnt.values())

# 산술평균
sys.stdout.write(format(sum(num_list) / N, '.0f') + '\n')
# 중앙값
sys.stdout.write(str(num_list[N // 2]) + '\n')
# 최빈값
temp = sorted([key for key, value in num_cnt.items() if value == commom_count])
sys.stdout.write(str(temp[1]) + '\n') if len(temp) > 1 else sys.stdout.write(str(temp[0]) + '\n')
#범위
sys.stdout.write(str(num_list[-1]-num_list[0]) + '\n')