import sys

def input():
    return sys.stdin.readline().rstrip()

X, Y = map(int, input().split())
cnt = 0
while X < Y:
    if Y % 10 == 1:
        Y = int(Y / 10)
        cnt += 1
    elif Y % 2 == 0:
        Y = Y / 2
        cnt += 1
    else:
        print(-1)
        exit()
    
if X == Y:
    print(cnt + 1)
else:
    print(-1)
