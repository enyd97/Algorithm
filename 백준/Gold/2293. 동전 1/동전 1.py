import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

coins = []
dp = [0] * (K + 1)

for _ in range(N):
    a = int(input())
    if a <= K:
        coins.append(a)


coins.sort()

dp[0] = 1
for coin in coins:
    for i in range(coin, K + 1):
        dp[i] += dp[i-coin]

print(dp[K])