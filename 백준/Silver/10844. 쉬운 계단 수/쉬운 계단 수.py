import sys

MOD = 1_000_000_000

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

dp = [[0, 0] for _ in range(101)]

dp = [[0 for _ in range(10)] for _ in range(101)]

for i in range (1, 10):
    dp[1][i] = 1    

for i in range(2, N + 1):
    for j in range(10):
        if j - 1 >= 0:
            dp[i][j] += dp[i-1][j-1] % MOD
        if j + 1 < 10:
            dp[i][j] += dp[i-1][j+1] % MOD

print(sum(dp[N])%MOD)
