from collections import deque
import sys


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    queue = deque([])
    N = int(input())

    for _ in range(N):
        current = input().split()
        command = current[0]

        if command == 'push_front':
            queue.appendleft(current[1])

        elif command == 'push_back':
            queue.append(current[1])

        elif command == 'pop_front':
            if queue:
                print(queue.popleft())
            else:
                print(-1)

        elif command == 'pop_back':
            if queue:
                print(queue.pop())
            else:
                print(-1)

        elif command == 'size':
            print(len(queue))

        elif command == 'empty':
            if queue:
                print(0)
            else:
                print(1)

        elif command == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)

        elif command == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)

        else:
            pass