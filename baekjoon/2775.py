# baekjoon b2 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    room = [[i+1 for i in range(n)]]
    for i in range(1, k+1):
        room.append([])
        for j in range(1, n+1):
            room[i].append(sum(room[i-1][:j]))
    sys.stdout.write(str(room[k][n-1]) + '\n')
