from collections import deque
import sys

global index
global N
global stack
global result


def push():
    global N, index, stack
    if index <= N:
        stack.append(index)
        index += 1
        result.append('+')
    else:
        print('NO')
        exit()


def pop():
    global N, stack
    temp = stack.pop()
    result.append('-')


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    index = 1
    stack = deque([])
    target = deque([])
    N = int(input())
    result = deque([])
    stack.append(0)

    # make target array
    for _ in range(N):
        target.append(int(input()))

    for i in range(N):
        while target[i] > stack[-1]:
            push()
        if target[i] == stack[-1]:
            pop()
        if target[i] < stack[-1]:
            print('NO')
            exit()
    print(*result, sep='\n')