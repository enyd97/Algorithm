import sys

def input():
    return sys.stdin.readline().rstrip()

N, S = map(int, input().split())

_list = list(map(int, input().split()))


_list.sort()

def dfs(n, result, temp): # left length, current result, current index
    global count
    global S
    result += _list[temp] 
    if n == 1:  # 부분 수열 끝
        if result == S:
            count += 1
        return
    
    for i in range(temp + 1, len(_list) - (n-1) + 1):
        dfs(n-1, result, i)

count = 0

for i in range(1, N + 1):
    # 길이가 i인 부분 수열을 만든다.
    # 합이 S라면 count++
    for j in range(0, len(_list) + 1 - i):
        dfs(i, 0, j)

print(count)