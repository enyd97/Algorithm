import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    _list = list(map(int, input().split()))
    M = int(input())
    test_list = list(map(int, input().split()))
    _list.sort()

    for val in test_list:
        left = 0
        right = len(_list) - 1
        while left < right:
            mid = (left + right) // 2
            if val <= _list[mid]:
                right = mid
            else:
                left = mid + 1
        if _list[right] == val:
            print(1, end=' ')
        else:
            print(0, end=' ')