from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    queue = deque([])
    N = int(input())
    for i in range(1, N+1):
        queue.append(i)

    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    print(queue[0])