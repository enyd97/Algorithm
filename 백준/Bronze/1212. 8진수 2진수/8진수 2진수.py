import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

result = []       
        
N = input()
if N == '0':
    print(0)
    exit()
for i in N[::-1]:
    temp = int(i)
    for _ in range(3):
        result.append(temp % 2)
        temp = int(temp/2)

while(result[-1] == 0):
    result.pop()
    
print(*result[::-1],sep='')