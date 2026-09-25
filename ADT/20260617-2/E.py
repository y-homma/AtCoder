import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    N, Q = map(int, input().split())
    U = [tuple(map(int, input().split())) for _ in range(Q)]
    Base = [0] * Q
    Next = [-1] * Q
    currentMax = 0
    for i in range(Q):
        Base[i] = max(0, U[i][0] - currentMax)
        currentMax = max(currentMax, U[i][0])
    minQ = dict()
    S = SortedSet()
    S.add(U[Q-1][0])
    minQ[U[Q-1][0]] = Q-1
    for i in reversed(range(Q-1)):
        x, y = U[i]
        idx = S.bisect_left(y)
        if idx < len(S):
            target = S[idx]
            nextIdx = minQ[target]
            Next[i] = nextIdx

        S.add(x)
        minQ[x] = i
    
    for i in range(Q):
        nextIdx = Next[i]
        if nextIdx > -1:
            Base[nextIdx] += Base[i]
    print(*Base, sep="\n")
    
    return 0
                            
if __name__ == "__main__":
    solve() 