import sys
from collections import deque
import heapq

def input():
    return sys.stdin.readline().rstrip()

def solution(K):
    #print('check day ', K)
    if K > N:
        #print('today is bigger than N pass')
        return 0
    if (K + schedule[K][0]) > N + 1:
        #print('today''s job is too long')
        return solution(K+1)
    return max(schedule[K][1] + solution(K + schedule[K][0]), solution(K+1))


N = int(input())
schedule = []
schedule.append([0,0]) # dummy value for index 0
for _ in range(N):
    a, b = map(int, input().split())
    temp = []
    temp.append(a)
    temp.append(b)
    schedule.append(temp)
    
print(solution(1))