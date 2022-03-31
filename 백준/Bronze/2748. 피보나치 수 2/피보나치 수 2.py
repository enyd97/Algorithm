import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

_list=[0, 1]

N = int(input())

for i in range(2, N + 1):
    _list.append(_list[i - 2] + _list[i - 1])
print(_list[N])