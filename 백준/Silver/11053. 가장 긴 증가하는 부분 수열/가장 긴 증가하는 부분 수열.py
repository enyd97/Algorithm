import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

_list = list(map(int, input().split()))
dp = [-1 for _ in range(N)] # store maximum length permutation's length at that index 
for i in range(N):
    dp[i] = 1
    temp = 0
    for j in range(i):
        if _list[i] > _list[j]:
            temp = max(temp, dp[j])
        dp[i] = temp + 1
print(max(dp))