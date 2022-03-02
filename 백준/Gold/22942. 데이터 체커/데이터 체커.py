import sys
from collections import deque



def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    N = int(input())
    s = deque([])
    for i in range(N):
        x, r = map(int, input().split())
        s.append((x-r, i, 'open'))
        s.append((x+r, i, 'close'))
    sorted_list = sorted(s)
    s.clear()
    for i in range(N):
        temp = sorted_list[i]
        if temp[2] == 'open':
            s.append(temp)
        else:
            cur = s.pop()
            if cur[1] != temp[1]:
                print('NO')
                exit()
    print('YES')