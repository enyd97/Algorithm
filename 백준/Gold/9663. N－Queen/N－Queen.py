import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def func(current):
    global count
    global result
    # exit
    if len(result) == N:
        count += 1
    for i in range(1, N + 1):
        if i in result:
            continue
        for index, value in enumerate(result):
            if len(result) - index == abs(value - i):
                break
        else:
            result.append(i)
            func(i)
            result.pop()


N = int(input())
count = 0

if __name__ == '__main__':
    result = []
    func(0)

    print(count)
