import sys
from collections import deque
import heapq

def input():
    return sys.stdin.readline().rstrip()

def solution():
    M = int(input())
    min_heap = []
    max_heap = []
    _list = list(map(int, input().split()))
    input_num = M
    input_num = input_num - 10
    while input_num > 1:
        temp = list(map(int, input().split()))
        _list = _list + temp
        input_num = input_num - 10
    heapq.heapify(min_heap)
    heapq.heapify(max_heap)
    mid = _list[0]
    result = []
    result.append(mid)
    #print(_list)
    for i in range(1, M): # skip index 0
        #print('current num : ', _list[i])
        if mid > _list[i]:
            heapq.heappush(max_heap, _list[i] * (-1))
        else:
            heapq.heappush(min_heap, _list[i])
            
        if (i + 1) % 2 == 1:   # odd number
            #print('odd number', i + 1)
            #print('max haep : ', max_heap)
            #print('min heap : ', min_heap)
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, mid)
                mid = heapq.heappop(max_heap)
                mid = mid * (-1)
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, mid * (-1))
                mid = heapq.heappop(min_heap)
            else:
                pass
            #print('mid : ', mid)
            result.append(mid)
    R = len(result)
    print(R)
    #print('result : ', result)
    while 1:
        if R > 10:
            R = R - 10
            ten_result = result[0:10]
            result = result[10:]
            #_str = ' '.join(ten_result)
            #print(_str, end=' ')
            print(*ten_result)
        else:
            ten_result = result[:]
            #_str = ' '.join(ten_result)
            #print(_str, end=' ')
            print(*ten_result)
            break
    return

N = int(input())
for i in range(N):
    #print('iteration', i)
    solution()