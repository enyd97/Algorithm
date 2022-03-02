import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def check(operator_stack, current):
    # return 1 to push
    if len(operator_stack) == 0:
        return 1
    top = operator_stack.pop()


if __name__ == '__main__':
    expression = input()
    stack = deque([])
    operators = ['+', '-', '*', '/']
    priority = [1, 1, 2, 2]
    _dict = dict(zip(operators, priority))

    for i in range(len(expression)):
        cur = expression[i]
        if 64 < ord(cur) < 91:  # characters
            print(cur, end='')
        else:  # operators
            if len(stack) == 0:
                stack.append(cur)
            elif cur == '(':
                stack.append(cur)
            elif cur == ')':
                top = stack.pop()
                while top != '(':
                    print(top, end='')
                    top = stack.pop()
            elif (cur == '+') | (cur == '-'):
                top = stack.pop()
                while (top != '(') & (len(stack) != 0):
                    print(top, end='')
                    top = stack.pop()
                if top == '(':
                    stack.append(top)
                else:
                    print(top, end='')
                stack.append(cur)
            else:   # operator is * or /
                top = stack.pop()
                if (top == '+') | (top == '-') | (top == '('):
                    stack.append(top)
                else:
                    print(top, end='')

                stack.append(cur)
    while len(stack) != 0:
        print(stack.pop(), end='')
