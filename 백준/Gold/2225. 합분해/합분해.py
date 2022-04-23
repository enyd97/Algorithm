import sys

def input():
    return sys.stdin.readline().rstrip()

MOD = 1_000_000_000

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)]

# dp[3][2] 3을 만들 때, 2개의 값을 이용하는 경우의 수

for i in range(1, N + 1):
    dp[i][0] = 0
    dp[i][1] = 1

for i in range(1, K + 1):
    dp[0][i] = 1
    dp[1][i] = i
 
for i in range(2, N + 1):
    for j in range(2, K + 1):
        for k in range(i + 1):
            dp[i][j] += dp[k][j-1] % MOD
        
print(dp[N][K] % MOD)