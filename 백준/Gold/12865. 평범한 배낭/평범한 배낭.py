import sys

def input():
    return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
thing = []
dp = [[-1] * (100000 + 1) for _ in range(100 + 1)]


for i in range(N):
    a, b = map(int, input().split())
    if a > K:
        continue
    thing.append((a,b))

thing.sort(key= lambda x:x[0])
# 첫번째 물건에 대해서

if len(thing) ==0:
    print(0)
    exit(0)

a, b = thing[0]
dp[0][0] = 0
dp[0][a] = b

# 두번째 물건부터
for i in range(1, len(thing)):   # 물건
    w, v = thing[i]
    
    dp[i][0] = 0
    for x in range(1, K + 1): # kg
        if x-w < 0:
            if dp[i-1][x] != -1:
                dp[i][x] = dp[i-1][x]
        elif dp[i-1][x-w] == -1 & dp[i-1][x] == -1:
            continue
        elif dp[i-1][x-w] == -1:
            dp[i][x] = dp[i-1][x]
        elif dp[i-1][x] == -1:
            dp[i][x] = dp[i-1][x-w] + v
        else:
            dp[i][x] = max(dp[i - 1][x], dp[i-1][x - w] + v)

# print(*dp, sep='\n')
print(max(dp[len(thing) - 1]))