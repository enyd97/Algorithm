import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def func(before, pos):
    global count
    global result
    global temp

    if len(result) == temp:
        count += 1
        if count == N:
            print(*result, sep='')
            exit()
        return

    for i in range(pos - 1, before):
        if i in result:
            continue
        result.append(i)
        func(i, pos - 1)
        result.pop()


N = int(input())
result = []
count = -1
temp = 0

if __name__ == '__main__':

    while temp < 11:
        temp = temp + 1
        func(10, temp)

    print(-1)
