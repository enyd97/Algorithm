import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def func(current):
    # exit
    if len(result) == M:
        print(*result, sep=' ')
    for i in range(1, N + 1):
        if i in result:
            continue
        result.append(i)
        func(i)
        result.pop()


N, M = map(int, input().split())

if __name__ == '__main__':
    result = []
    func(0)