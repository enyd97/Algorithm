import sys
def input():
    return sys.stdin.readline().rstrip()

def solution(k):
    temp = 0
    result = 0
    while result < k:
        temp = temp + 1
        temp_str = str(temp)
        if '666' in temp_str:
            result = result + 1
            
    return temp

N = int(input())
print(solution(N))