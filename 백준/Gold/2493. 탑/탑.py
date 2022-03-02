import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    arr = deque([])
    s = deque([])
    tag = 0
    result = [0 for _ in range(N)]
    s.append((0, float('inf')))
    _list = list(map(int, input().split()))
    for i in range(N):
        arr.append((i+1, _list[i]))
    for i in range(N):
        top = arr.pop()
        if len(s) == 0:
            s.append(top)
            continue
        temp = s.pop()
        if temp[1] > top[1]:
            s.append(temp)
            s.append(top)
            continue
        while temp[1] < top[1]:
            result[temp[0] - 1] = top[0]
            temp = s.pop()
        s.append(temp)
        s.append(top)

    print(*result, sep=' ')