import sys
from collections import deque
from heapq import heapify, heappop, heappush
  
def solve():
    input = sys.stdin.readline 
    N, M =map(int, input().split())
    H = list(map(int, input().split()))
    E = [[] for _ in range(N)]
    INF = 1000000000000000
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].append((v-1, max(H[v-1] - H[u-1], 0)))
        E[v-1].append((u-1, max(H[u-1] - H[v-1], 0)))


    F = [INF] * N
    Q = [(0, 0)]
    heapify(Q)
    ans = 0
    while len(Q) > 0:
        f, ci = heappop(Q)
        if f < F[ci]:
            F[ci] = f
            ans = max(ans, H[0] - H[ci] - F[ci])
            # print(F)
            for ni, df in E[ci]:
                nf = f + df
                if F[ni] > nf:
                    heappush(Q, (nf, ni))
    print(ans)    
    
    
    return 0
  
if __name__ == "__main__":
    solve()