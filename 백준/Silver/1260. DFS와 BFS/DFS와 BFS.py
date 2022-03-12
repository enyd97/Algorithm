import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

result = []

def dfs(X):
    
    visited[X] = 1
    result.append(X)
    for next in graph[X]:
        if not visited[next]:
            dfs(next)

def bfs(X):
    Q = deque()
    visited[X] = 1
    Q.append(X)
    result.append(X)
    while Q:
        node = Q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1
                Q.append(next)
                result.append(next)
            

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()
    
    
dfs(V)
print(*result, sep=' ')
visited = [0] * (N + 1)
result = []

bfs(V)
print(*result, sep=' ')