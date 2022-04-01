import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

_list = []

for _ in range(N):
    x, y = map(int, input().split())
    time  = y - x
    _list.append([x, y])
    
_list.sort(key= lambda x = x:(x[1], x[0]))

cnt = 0
result = [[0,0]]
for current in _list:
    if result[-1][1] <= current[0]:
        result.append(current)
        cnt += 1
    else:
        continue

print(cnt)