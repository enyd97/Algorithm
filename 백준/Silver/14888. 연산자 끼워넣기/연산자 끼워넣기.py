import sys
from itertools import permutations
import math


def input():
    return sys.stdin.readline().rstrip()


def operate(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    else:
        if a < 0:
            return -int(-a/b)
        return int(a/b)


if __name__ == '__main__':
    N = int(input())
    maximum = -math.inf
    minimum = math.inf
    _list = list(map(int, input().split()))
    plus, sub, mul, div = map(int, input().split())
    operators = []
    for _ in range(plus):
        operators.append('+')
    for _ in range(sub):
        operators.append('-')
    for _ in range(mul):
        operators.append('*')
    for _ in range(div):
        operators.append('/')
    temp = list(set(list(permutations(operators))))

    for i in range(len(temp)):
        temp_op = list(temp[i])
        result = _list[0]

        for j in range(1, N):
            result = operate(result, _list[j], temp_op[j-1])

        maximum = max(result, maximum)
        minimum = min(result, minimum)
    print(maximum)
    print(minimum)

