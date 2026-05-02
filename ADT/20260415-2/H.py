import sys
from collections import deque
import heapq

  
def solve():
    input = sys.stdin.readline 
    N, X, Y = map(int, input().split())
    Bus = [list(map(int, input().split())) for _ in range(N-1)]
    INF = 10 ** 15
    T = [[INF for _ in range(840)] for i in range(N)]
    for t in range(840):
        T[0][t] = X + t
    for i in range(1, N):
        p, move = Bus[i-1]
        for t in range(840):
            pre = T[i-1][t]
            if pre == INF: continue
            mod = pre % p
            start = pre
            if mod > 0:
                start += p - mod
            T[i][t] = min(T[i][t], start + move)
    
    Q = int(input())
    ans = [INF for _ in range(Q)]
    for i in range(Q):
        q = int(input())
        mod = q % 840
        ans[i] = q - mod + T[N-1][mod] + Y
    print(*ans, sep="\n")

    return 0
  
if __name__ == "__main__":
    solve()