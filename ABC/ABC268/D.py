import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import permutations
from bisect import bisect_left

def binary_search(L, x):
    i = bisect_left(L, x)
    if i != len(L) and L[i] == x:
        return i
    return -1
  
def solve():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    S = [input().strip("\n") for _ in range(N)]
    T = [input().strip("\n") for _ in range(M)]
    T.sort()
    length = N-1
    for s in S:
        length += len(s)
    extraDash = 16 - length   
    A = []

    def dfs(idx, SL, remain, ans):
        if remain < 0:
            return False
        
        if idx == N:
            if len(ans) >= 3 and binary_search(T, ans) == -1:
                A.append(ans)
                return True
            return False

        if len(ans) > 0 and ans[-1] != "_":
            isFin = dfs(idx, SL, remain, ans + "_")
            return isFin
        else:
            isFin = dfs(idx+1, SL, remain, ans + SL[idx])
            if not isFin and len(ans) > 0:
                isFin = dfs(idx, SL, remain-1, ans + "_")
            return isFin

    L = [i for i in range(N)]
    for p in permutations(L):
        NS = [S[p[i]] for i in range(N)]
        dfs(0, NS, extraDash, "")
        if len(A) > 0:
            print(A[0])
            break
    else:
        print(-1)
    return 0
  
if __name__ == "__main__":
    solve()