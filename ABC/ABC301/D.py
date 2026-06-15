import sys
# from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
# sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    S = input().strip("\n")
    N = int(input())
    L = len(S)
    QI = []
    base = 0
    for i in range(L):
        if S[i] == "1":
            base |= 1 << L-i-1
        elif S[i] == "?":
            QI.append(i)
    if base > N:
        print(-1)
        return 0
    
    for i in QI:
        add = 1 << L-i-1
        if (base | add) <= N:
            base |= add
    print(base)
    
    return 0
                            
if __name__ == "__main__":
    solve() 