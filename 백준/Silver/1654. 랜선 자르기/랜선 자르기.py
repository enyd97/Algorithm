import sys

def input():
    return sys.stdin.readline().rstrip()
    
def func(length, cables):
    count = 0
    for temp in cables:
        count += temp // length
    return count
    
if __name__ == "__main__":
    K, N = map(int, input().split())
    _list = [int(input()) for i in range(K)]
    
    left = 0
    right = 2**31 - 1
    
    while left <= right:
        mid = (left + right) // 2
        if func(mid, _list) < N: # fail to make N cables 
            right = mid - 1 #need smaller mid
        else:   # possible to make N and more cables
            answer = mid
            left = mid + 1
            
    print(answer)