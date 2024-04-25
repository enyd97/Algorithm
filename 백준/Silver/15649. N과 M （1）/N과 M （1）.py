import sys
from collections import deque
import heapq


def input():
    return sys.stdin.readline().rstrip()

def solution(k):
    if len(result) == M:
        return
    else:
        if k in result:
            pass
        else:
            result.append(k)
            if len(result) == M:
                print(*result)
            for i in range(1, N + 1):
                solution(i)
            result.remove(k)
    return 

N, M = map(int, input().split())
    
result = []
for i in range(1, N + 1):
    solution(i)
