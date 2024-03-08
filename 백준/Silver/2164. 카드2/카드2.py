import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def solution(N):
    q = deque()
    for i in range(1, N+1):
        q.append(i)
    if len(q)==1:
        return q[0]
    q.popleft()
    while len(q) >1:    
        temp = q[0]
        q.popleft()
        q.append(temp)
        q.popleft()
    return q[0]
    
num = int(input())
print(solution(num))