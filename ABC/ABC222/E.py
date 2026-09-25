import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
# import bisect
sys.setrecursionlimit(10**6)
    
def solve():
    input = sys.stdin.readline 
    mod = 998244353
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    E = [[] for _ in range(N)]
    Path = {}
    for _ in range(N-1):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
        Path[(min(u-1, v-1), max(u-1, v-1))] = 0
    Parents = [-1] * N
    Depth = [-1] * N
    Q = deque()
    Q.append((0, 1, 0))
    while len(Q) > 0:
        idx, depth, parent = Q.popleft()
        if Depth[idx] == -1:
            Parents[idx] = parent
            Depth[idx] = depth
            for ne in E[idx]:
                if ne != parent:
                    Q.append((ne, depth + 1, idx))
    
    for i in range(M-1):
        cn = A[i] - 1
        nn = A[i+1] - 1
        if Depth[cn] < Depth[nn]:
            cn, nn = nn, cn
        while Depth[nn] < Depth[cn]:
            cnp = Parents[cn]
            Path[(min(cn, cnp), max(cn, cnp))] += 1
            cn = cnp
        
        while cn != nn:
            cnp = Parents[cn]
            Path[(min(cn, cnp), max(cn, cnp))] += 1
            cn = cnp

            nnp = Parents[nn]
            Path[(min(nn, nnp), max(nn, nnp))] += 1
            nn = nnp
    
    Base = 10 ** 5
    DP = [0] * (2 * Base + 1) # -Base = 0, 0 = Base, +Base = 2Base
    P = [Path[i] for i in Path.keys()]
    DP[Base + P[0]] += 1 # R
    DP[Base - P[0]] += 1 # B
    for i in range(1, N-1):
        count = P[i]
        nDP = [0] * (2 * Base + 1)
        for j, prev in enumerate(DP):
            if prev > 0:
                nDP[j-count] += prev
                nDP[j-count] %= mod
                nDP[j+count] += prev
                nDP[j+count] %= mod
        DP = nDP
    print(DP[Base + K] % mod)
    # print(Path)
                            
if __name__ == "__main__":
    solve() 
