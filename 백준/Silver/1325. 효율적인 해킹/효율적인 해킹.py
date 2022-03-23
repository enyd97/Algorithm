import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def bfs(X):
    temp = 0
    Q = deque()    
    visited[X] = 1
    Q.append(X)
    temp += 1
    while Q:
        node = Q.popleft()
        for next in graph[node]:
            if not visited[next]:
                temp += 1
                visited[next] = 1
                Q.append(next)
    return temp
            

N, M = map(int, input().split())

result = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, N + 1):
    result[i] = bfs(i)
    visited = [0 for _ in range(N + 1)]

max = max(result)
_list = [i for i, element in enumerate(result) if element == max]

print(*_list)