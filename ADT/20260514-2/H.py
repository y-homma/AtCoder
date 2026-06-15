import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from math import sqrt
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    A = list(map(int, input().split()))
    # 平均値を求める
    MINF = -1000000000000000
    L = max(A)
    low = 1
    high = L
    while high - low > 0.0001 * L:
        mid = sqrt(low * high)

        DP0 = 0
        DP1 = A[0] - mid
        for i in range(1, N):
            mp = max(DP0, DP1)
            DP0 = DP1
            DP1 = mp + A[i] - mid
        if max(DP0, DP1) >= 0:
            low = mid
        else:
            high = mid
       # print(f"Mid: {mid}, Max: {max(DP[N-1])}")
    print(low)

    low = 1
    high = L
    while high >= low:
        mid = (high + low) >> 1
        DP0 = 0
        DP1 = 1 if A[0] >= mid else -1
        for i in range(1, N):
            d = 1 if A[i] >= mid else -1
            mp = max(DP0, DP1)
            DP0 = DP1
            DP1 = mp + d
        if max(DP0, DP1) > 0:
            low = mid + 1
        else:
            high = mid - 1
    print(high)
    
    return 0
  
if __name__ == "__main__":
    solve()