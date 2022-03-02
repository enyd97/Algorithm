import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    expression = input()
    _dict = {}
    stack = deque([])
    for i in range(N):
        _dict[chr(65 + i)] = int(input())

    for i in range(len(expression)):
        if expression[i] == '+':
            A = stack.pop()
            B = stack.pop()
            stack.append(A + B)
        elif expression[i] == '-':
            A = stack.pop()
            B = stack.pop()
            stack.append(B - A)
        elif expression[i] == '*':
            A = stack.pop()
            B = stack.pop()
            stack.append(A * B)
        elif expression[i] == '/':
            A = stack.pop()
            B = stack.pop()
            stack.append(B / A)
        else:
            stack.append(_dict[expression[i]])

    print("{:.2f}".format(float(stack.pop())))