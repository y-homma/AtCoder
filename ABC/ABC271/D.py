import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import permutations

def solve():
    input = sys.stdin.readline 
    N, S = map(int, input().split())
    C = [tuple(map(int, input().split())) for _ in range(N)]
    DP = [[False] * (S + 1) for _ in range(N)]
    BIT = [[0] * (S + 1) for _ in range(N)] #1が表
    s = C[0]
    if s[0] <= S:
        DP[0][s[0]] = True
        BIT[0][s[0]] = 1
    if s[1] <= S:
        DP[0][s[1]] = True
    

    for i, s in enumerate(C[1:]):
        a = s[0]
        b = s[1]
        bit = pow(2, i+1)
        for j in range(1, S+1):
            if DP[i][j]:
                base = BIT[i][j]
                if a + j <= S:
                    DP[i+1][a+j] = True
                    BIT[i+1][a+j] = base + bit
                if b + j <= S:
                    DP[i+1][b+j] = True
                    BIT[i+1][b+j] = base
    if DP[N-1][S]:
        print("Yes")
        bit = BIT[N-1][S]
        ans = [""] * N
        for j in range(N):
            ans[j] = "H" if bit % 2 == 1 else "T"
            bit >>= 1
        print(*ans, sep="")
    else:
        print("No")
                

    return 0
  
if __name__ == "__main__":
    solve()