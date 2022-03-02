import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def func(date, remain, money):
    global N
    # exit
    if date >= N:
        if remain > 0:
            return 0
        return money

    result = func(date + 1, remain - 1, money)
    if remain > 0:
        return result
    return max(result, func(date + 1, T[date] - 1, money + P[date]))


N = int(input())

if __name__ == '__main__':

    T = []
    P = []
    for i in range(N):
        a ,b = map(int, input().split())
        T.append(a)
        P.append(b)

    print(func(0, 0, 0))