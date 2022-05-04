import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

result = []       
        
N = int(input())
result = []
for _ in range(N):
    temp = int(input())
    _list = list(map(int, input().split()))
    MIN = _list[0]
    MAX = _list[0]
    for j in range(1, temp):
        if _list[j] > MAX:
            MAX = _list[j]
        if _list[j] < MIN:
            MIN = _list[j]
    result.append([MIN, MAX])

for i in range(N):
    print(*result[i], sep=' ')      