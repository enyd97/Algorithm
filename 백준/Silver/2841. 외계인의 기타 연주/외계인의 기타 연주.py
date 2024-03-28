import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    global result
    string, plat = map(int, input().split())
    if not string_que[string]:          # if string que is empty just put plat
        string_que[string].append(plat)
        result = result + 1
    elif string_que[string][-1] < plat:
        string_que[string].append(plat)
        result = result + 1
    elif string_que[string][-1] > plat:
        while string_que[string][-1] > plat:
            string_que[string].pop()
            result = result + 1
            if not string_que[string]:
                string_que[string].append(plat)
                result = result + 1
                return
        if string_que[string][-1] == plat:
            pass
        else:
            string_que[string].append(plat)
            result = result + 1
    
    return
        
melody_num, plat_len = map(int, input().split())
string_que = []
result = 0
for i in range(7):
    string_que.append(deque())

for i in range(melody_num):
    solution()

print(result)