import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    MINF = -1 * 10 ** 20
    DP = [[MINF] * (M+1) for _ in range(N)]
    for i in range(N): DP[i][0] = 0
    DP[0][1] = A[0]
    for i in range(1, N):
        a = A[i]
        for j in range(1, min(i+2, M+1)):
            DP[i][j] = max(DP[i-1][j-1] + j * a, DP[i-1][j])
    print(DP[N-1][M])
    return 0
  
if __name__ == "__main__":
    solve()