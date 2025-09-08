import sys
import collections
from collections import deque
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    mod = 7 + 10 ** 9
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    E = [[] for _ in range(M)]
    for i in range(M):
        u, v = map(int, input().split())
        E[i] = (u - 1, v - 1)

    
    DP =[INF] * N
    tmp = [INF] * N
    DP[0] = 0
    for i in reversed(range(1, N)):
        tmp = DP
        DP = [INF] * N
        DP[0] = 0
        for u, v in E:
            DP[u] = min(DP[u], tmp[v] + W[v] * i)
            DP[v] = min(DP[v], tmp[u] + W[u] * i)
    
    print(*DP, sep="\n")
    return 0
  
if __name__ == "__main__":
    solve()