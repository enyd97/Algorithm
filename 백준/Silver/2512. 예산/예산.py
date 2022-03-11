import sys

def input():
    return sys.stdin.readline().rstrip()
    
def func(current, _list):
    count = 0
    for temp in _list:
        count += (temp if temp < current else current) 
    return count
    
if __name__ == "__main__":
    N = int(input())
    _list = list(map(int,input().split()))
    Total = int(input())
    
    if sum(_list) <= Total:
        print(max(_list))
        exit()
              
    left = 0
    right = 1000000000
    
    while left < right:
        mid = (left + right) // 2
        if func(mid, _list) > Total:
            right = mid
        else:
            answer = mid
            left = mid + 1
            
    print(answer)