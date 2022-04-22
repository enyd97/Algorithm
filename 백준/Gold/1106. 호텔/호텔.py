import sys

DEFAULT = int(1e9)

def input():
    return sys.stdin.readline().rstrip()

C, N = map(int, input().split())

cities = []


for _ in range(N):
    a, b = map(int, input().split())
    cities.append((a, b)) # (cost, customer)


dp = [DEFAULT] * (C + 1 + 100)

dp[0] = 0
for i in range(1, C + 100 + 1):
    result= DEFAULT
    for temp in cities:
        if i - temp[1] >= 0:
            result = min(result, dp[i-temp[1]] + temp[0])
    dp[i] = result
print(min(dp[C:C + 100]))
