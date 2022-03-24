import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(X, Y):
    Q = deque()    
    visited[X][Y] = 1
    Q.append((X, Y))
    while Q:
        X, Y = Q.popleft()
        for i in range(4):
            x = X + dx[i]
            y = Y + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if visited[x][y] == -1 and graph[x][y] == '1':
                    visited[x][y] = visited[X][Y] + 1
                    Q.append((x, y))
            

N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
bfs(0, 0)

print(visited[N-1][M-1])
