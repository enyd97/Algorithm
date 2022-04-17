import sys

DEFAULT = int(1e9)

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coins = []
value = [-1] * (100001)

for i in range(n):
    coins.append(int(input()))

for temp in coins:
    value[temp] = 1

for i in range (1, k + 1):
    if i in coins:
        continue
    result = DEFAULT
    for j in coins:
        if i - j < 0:
            continue
        if value[i - j] == -1:
            continue
        result = min(value[i-j], result)
    if result != DEFAULT:
        value[i] = result + 1
        
        
print(value[k])