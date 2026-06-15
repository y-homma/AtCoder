import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import permutations


  
def solve():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    S = [input().strip("\n") for _ in range(N)]
    T = [input().strip("\n") for _ in range(M)]
    length = N-1
    for s in S:
        length += len(s)
    extraDash = 16 - length    

    L = [i for i in range(N)]
    for p in permutations(L):
        NS = [S[p[i]] for i in range(N)]
        name = "_".join(NS)
        for t in T:
            if t == name:
                break
        else:
            print(name)
            return 0
    print(-1)
    return 0
  
if __name__ == "__main__":
    solve()