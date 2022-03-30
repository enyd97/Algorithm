import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    Q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:  # starting point, tomato here
                visited[i][j] = 0
                Q.append((i, j))
    while Q:
        X, Y = Q.popleft()
        for i in range(4):
            x = X + dx[i]
            y = Y + dy[i]
            if 0 <= x < N and 0 <= y < M:
                if graph[x][y] == 0:
                    if visited[x][y] == -1: #first visit
                        visited[x][y] = visited[X][Y] + 1
                        Q.append((x, y))
                    else:
                        if visited[x][y] > visited[X][Y] + 1:
                            visited[x][y] = visited[X][Y] + 1
                            Q.append((x, y))                   
                        
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
# 3 dimention - first and second dimention - x, y third dimension - show if it was already visitied
# if the point is first visited, visitied[x][y][0] is -1.
# if the point is already visited, visited[x][y][0] is not -1, and we use visited[x][y][1]

bfs()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j]== -1:
            print(-1)
            exit()
print(max(map(max, visited)))