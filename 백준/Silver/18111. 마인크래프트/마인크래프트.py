import sys
from collections import deque
import heapq

def input():
    return sys.stdin.readline().rstrip()

def solution():
    low = min(map(min,house_area))
    high = max(map(max,house_area))
    
    result_time = 99999999999
    for floor in range(low, high + 1):

        block = B
        time = 0
        for i in range(N):
            for j in range(M):
                temp = house_area[i][j]
                if temp < floor:
                   gap = floor - temp
                   time = time + gap
                   block = block - gap
                else:
                    gap = temp - floor
                    time = time + 2 * gap
                    block = block + gap

        if block < 0:
            time = 99999999999
        if time <= result_time:
            result_time = time
            result_floor = floor
        
    return result_time, result_floor

N, M, B = map(int, input().split())
house_area=[]

for _ in range(N):
    temp = list(map(int, input().split()))

    house_area.append(list(temp))

    
a, b= solution()
print(a, b)