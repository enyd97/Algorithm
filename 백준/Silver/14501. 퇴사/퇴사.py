import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(K):
    if K > N:
        return 0
    if (K + schedule[K][0]) > N + 1:
        return solution(K+1)
    return max(schedule[K][1] + solution(K + schedule[K][0]), solution(K+1))

N = int(input())
schedule = []
schedule.append([0,0])
for _ in range(N):
    a, b = map(int, input().split())
    temp = []
    temp.append(a)
    temp.append(b)
    schedule.append(temp)
    
print(solution(1))