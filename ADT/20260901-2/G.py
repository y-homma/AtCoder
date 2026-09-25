import sys
from collections import deque
from itertools import permutations
from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    mod = 998244353
    T = input().strip("\n")
    L = len(T)
    N = int(input())
    B = [[] for _ in range(N)]
    for i in range(N):
        query = list(map(str, input().strip("\n").split()))
        B[i] = query[1:]
    INF = 100000000000000
    DP = [INF for _ in range(L)]

    for s in B[0]:
        size = len(s)
        if s == T[:size]:
            DP[size-1] = 1

    for i in range(1, N):
        ND = [INF] * L
        for k, d in enumerate(DP):
            ND[k] = d
        for s in B[i]:
            size = len(s)
            for j in range(L):
                if s == T[j:j+size]:
                    if j == 0:
                        ND[size-1] = min(ND[size-1], 1)
                    elif DP[j-1] < INF:
                        ND[j+size-1] = min(ND[j+size-1], 1 + DP[j-1])
        for k, d in enumerate(ND):
            DP[k] = d
        # print(DP)

    print(DP[L-1] if DP[L-1] < INF else -1)
    
    return 0
                            
if __name__ == "__main__":
    solve() 