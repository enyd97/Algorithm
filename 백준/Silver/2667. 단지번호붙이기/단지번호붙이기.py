import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(X, Y):
    if visited[X][Y] == 0 and graph[X][Y] == '1':
        Q = deque()    
        visited[X][Y] = 1
        cnt.append(1)
        Q.append((X, Y))
        while Q:
            X, Y = Q.popleft()
            for i in range(4):
                x = X + dx[i]
                y = Y + dy[i]
                if 0 <= x < N and 0 <= y < N:
                    if visited[x][y] == 0 and graph[x][y] == '1':
                        visited[x][y] =  1
                        cnt[-1] += 1
                        Q.append((x, y))
            

N = int(input())
cnt = []
graph = [list(input()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        bfs(i, j)        

cnt.sort()        
            
print(len(cnt))
print(*cnt, sep='\n')