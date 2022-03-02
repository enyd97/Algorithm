import sys
from itertools import combinations
import math


def input():
    return sys.stdin.readline().rstrip()


if __name__ == '__main__':
    result = math.inf
    N = int(input())
    stat = [list(map(int, input().split())) for i in range(N)]
    arr = [i for i in range(N)]
    combi = list(combinations(arr, math.floor(N/2)))
    for i in range(len(combi)):
        i1 = combi[i]
        i2 = [x for x in arr if x not in i1]
        team1 = 0
        team2 = 0
        for a, b in list(combinations(i1, 2)):
            team1 += stat[a][b] + stat[b][a]
        for a, b in list(combinations(i2, 2)):
            team2 += stat[a][b] + stat[b][a]
        result = min(result, abs(team1 - team2))
    print(result)