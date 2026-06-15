import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import permutations

def solve():
    input = sys.stdin.readline 
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    DP = [0 for _ in range(N+1)]
    DP[1] = 1
    for i in range(2, N+1):
        maxS = 0
        for k, a in enumerate(A):
            if a > i: break
            maxS = max(a + (i - a) - DP[i-a], maxS)
        DP[i] = maxS
    print(DP[N])

    return 0
  
if __name__ == "__main__":
    solve()