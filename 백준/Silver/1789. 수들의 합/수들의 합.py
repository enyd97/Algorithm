import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    S = int(input())
    # left = 1
    # right = S
    # mid = 1
    temp = 0
    i = 0
    while 1:
        i += 1
        temp = temp + i
        if temp > S:
            print(i-1)
            exit()