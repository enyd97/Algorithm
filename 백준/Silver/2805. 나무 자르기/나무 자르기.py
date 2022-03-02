import sys


def input():
    return sys.stdin.readline().rstrip()


def func(height, trees):
    count = 0
    for temp in trees:
        if temp - height > 0:
            count += temp - height
    return count


if __name__ == '__main__':
    tree_num, Need = map(int, input().split())
    _list = list(map(int, input().split()))
    left = 0
    right = 1000000000
    while left <= right:
        mid = (left + right) // 2
        if func(mid, _list) < Need:
            right = mid - 1
        else:
            left = mid + 1
    print(right)