from collections import deque

if __name__ == '__main__':
    N, K = map(int, input().split())
    Q = deque([])
    result = []
    for i in range(N):
        Q.append(i+1)
    count = 0
    while Q:
        count = count + 1
        if not count % K:
            result.append(Q.popleft())
        else:
            Q.append(Q.popleft())

    print('<' + ', '.join(map(str, result)) + '>')