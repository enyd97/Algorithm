import sys
from collections import deque
import re

def input():
    return sys.stdin.readline().rstrip()

def solution():
    func = list(input())
    length = int(input())
    nums = input()
    numbers = re.findall(r'\d+', nums)
    if func.count('D') > length:
        print_list.append('error')
        return 
    if length == 0:
        print_list.append('[]')
        return   
    q = deque()
    for temp in numbers:
        if temp.isdigit():
            q.append(temp)
    dir = 1
    for operation in func:
        if operation == 'R':
            dir = dir * (-1)
        else:
            if dir == 1:
                q.popleft()
            else:
                q.pop()
    result = '['
    if len(q) == 0:
        print_list.append('[]')
        return
    while len(q) > 1:
        if dir == 1:
            temp = q.popleft()
            result = result + str(temp)
        else:
            temp = q.pop()
            result = result + str(temp)
        result = result + ','
    result =  result + str(q.pop()) + ']'
    print_list.append(result)
    return
        
T=int(input())
print_list = []
for i in range(T):
    solution()

for i in range(T):
    print(print_list[i])
 