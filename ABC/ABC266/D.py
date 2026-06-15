import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    L = 10 ** 5 + 1
    MINF = -10000000000
    DP = [[0, 0, 0, 0, 0] for _ in range(L)]
    for s in S:
        t, x, a = s
        DP[t][x] = a

    DP[0][1] = DP[0][2] = DP[0][3] = DP[0][4] = MINF
    DP[1][2] = DP[1][3] = DP[1][4] = MINF
    DP[2][3] = DP[2][4] = MINF
    DP[3][4] = MINF
    
    for i in range(1, L):
        for j in range(5):
            maxPre = 0
            for k in range(-1, 2):
                pre = j + k
                if 0 <= pre <= 4:
                    maxPre = max(maxPre, DP[i-1][pre])
            DP[i][j] += maxPre
    print(max(DP[L-1]))

    return 0
  
if __name__ == "__main__":
    solve()