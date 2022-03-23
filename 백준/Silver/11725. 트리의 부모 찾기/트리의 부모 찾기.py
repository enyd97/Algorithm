import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def bfs(X):
    Q = deque()    
    visited[X] = 1
    Q.append(X)
    while Q:
        node = Q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1
                parent[next] = node
                Q.append(next)
            

N = int(input())

result = [0 for _ in range(N)]
graph = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]
parent = [0 for _ in range(N + 1)]

for i in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    
bfs(1)
for i in range(2, N + 1):
    print(parent[i])