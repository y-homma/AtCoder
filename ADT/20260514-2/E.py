import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import permutations
  
def solve():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    E = [[-1 for j in range(N)] for _ in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        E[a][b] = c
        E[b][a] = c

    t = [i for i in range(N)]
    ans = 0
    for p in permutations(t):
        ci = p[0]
        dist = 0
        for i in range(1, N):
            ni = p[i]
            if E[ci][ni] == -1:
                break
            else:
                dist += E[ci][ni]
                ci = ni
        ans = max(ans, dist)
    print(ans)
    
    return 0
  
if __name__ == "__main__":
    solve()