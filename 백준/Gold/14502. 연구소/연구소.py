import sys
from collections import deque
from itertools import combinations
import copy

def input():
    return sys.stdin.readline().rstrip()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    Q = deque()
    for i in range(M):
        for j in range(N):
            if temp_graph[i][j] == 2:  # starting point
                visited[i][j] = 0
                Q.append((i, j))
            elif temp_graph[i][j] == 1:  # wall
                visited[i][j] = 0
    while Q:
        X, Y = Q.popleft()
        for i in range(4):
            x = X + dx[i]
            y = Y + dy[i]
            if 0 <= x < M and 0 <= y < N:
                if temp_graph[x][y] == 0 and visited[x][y] == 1:
                    visited[x][y] = 0
                    Q.append((x, y))   
                        
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]

result = []
empty_space = []

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            empty_space.append((i, j))
            
walls = list(combinations(empty_space, 3))

for current_wall in walls:
    wall1, wall2, wall3 = current_wall
    wall1_x, wall1_y = wall1
    wall2_x, wall2_y = wall2
    wall3_x, wall3_y = wall3

    temp_graph = copy.deepcopy(graph)

    temp_graph[wall1_x][wall1_y] = 1
    temp_graph[wall2_x][wall2_y] = 1
    temp_graph[wall3_x][wall3_y] = 1
    visited = [[1 for _ in range(N)] for _ in range(M)]
    bfs()
    result.append(sum([sum(visited[i]) for i in range(M)])) 

print(max(result))
