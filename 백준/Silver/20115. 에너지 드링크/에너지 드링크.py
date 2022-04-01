import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
_list = list(map(int, input().split()))

_list.sort()
result = _list[N - 1]
for i in range(N - 1):
    result += _list[i] / 2

print(result)