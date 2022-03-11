import sys

def input():
    return sys.stdin.readline().rstrip()

result = []

def dfs(X):
    result.append(1)
    visited[X] = 1
    for next in graph[X]:
        if not visited[next]:
            dfs(next)

if __name__ == "__main__":
    Num_com = int(input())
    Num_pair = int(input())
    
    graph = [[] for _ in range(Num_com + 1)]
    visited = [0] * (Num_com + 1)
    for i in range(Num_pair):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    dfs(1)
    print(sum(result)-1)