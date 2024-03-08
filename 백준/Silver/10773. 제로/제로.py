import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def solution():
    s = deque()
    n = int(input())
    for i in range(n):
        k = int(input())
        if k == 0:
            s.pop()
        else:
            s.append(k)
    sum = 0
    for i in s:
        sum = sum + i 
    return sum
        
    
print(solution())