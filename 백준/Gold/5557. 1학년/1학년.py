import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

_list = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(N - 1)]

dp[0][_list[0]] = 1

for i in range(0, N - 2):
    temp = _list[i + 1]
    for j in range(0, 21):
        if dp[i][j] != 0:
            if j + temp <= 20:
                dp[i+1][j + temp] += dp[i][j]
            if j - temp >= 0:
                dp[i+1][j - temp] += dp[i][j]
                
print(dp[-1][_list[-1]])