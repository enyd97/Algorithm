import sys
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    arr = [i + 1 for i in range(N)]
    result = list(permutations(arr))
    for i in range(len(result)):
        print(*result[i], sep=' ')