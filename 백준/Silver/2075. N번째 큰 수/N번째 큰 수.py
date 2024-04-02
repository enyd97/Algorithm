import sys
from collections import deque
import heapq

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)
    for _ in range(N-1):
        temp = list(map(int, input().split()))
        for j in range(N):
            min_value = heapq.heappop(heap)
            max_val = max(temp[j], min_value)
            heapq.heappush(heap, max_val)
    return min(heap)
        
print(solution())