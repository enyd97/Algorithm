import sys

MOD = 15746

def input():
    return sys.stdin.readline().rstrip()

N = int(input())

_list = [0] * (N + 1)
    
_list[0] = 1
_list[1] = 2

# 1 : 1
# 2 : 00 11
# 3 : 100 001 111
# 4 : 1100 1001 1111 0011 0000
# 5 : 11111 11100 11001 10011 00111 10000 00100 00001 

for i in range(2,N):
    _list[i] = (_list[i-1] + _list[i-2]) % 15746  
print(_list[N-1])