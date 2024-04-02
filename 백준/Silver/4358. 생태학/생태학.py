import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution():
    whole = 0
    while True:
        temp = input()
        if temp == "":
            break
        whole = whole + 1
        if not temp in trees.keys():
            trees[temp] = 1
        else:
            trees[temp] = trees[temp] + 1    
    
    new_trees = sorted(trees.items())
    for i in range(len(new_trees)):
        a, b = new_trees[i]
        print(a + ' {:.4f}'.format(b/whole*100))
    return
        
trees = {}
solution()