import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, M = map(int, input().split())
    result = 0
    for _ in range(N):
        temp = input()
        first[temp] = True
    
    for _ in range(M):
        temp = input()
        if temp in first:
            result = result + 1
        
    return result
        
first = {}

print(solution())