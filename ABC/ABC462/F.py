import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    T = int(input())
    INF = 10 ** 6
    for t in range(T):
        S = input().strip("\n")
        L = len(S)
        K = int(input())
        X = [0] * (L+1)
        Y = [0] * (L+1)
        Z = [0] * (L+1)
        DP = [[INF] * (K+1) for _ in range(L+1)]
        for i in range(3, L+1):
            if S[i-3] != "A": Y[i] += 1
            if S[i-2] != "B": Y[i] += 1
            if S[i-1] != "C": Y[i] += 1
            if Y[i] == 0: Z[i] += 1
            for j in range(0, 3):
                if i + j <= L: X[i+j] += Z[i]
        DP[0][0] = 0
        for i in range(1, L+1):
            DP[i][0] = 0
            for k in range(1, K+1):
                if k + Z[i] <= K:
                    DP[i][k] = min(DP[i][k], DP[i-1][k+Z[i]])
                if i >= 3:
                    DP[i][k] = min(DP[i][k], DP[i-3][k-1+X[i]] + Y[i])
        if DP[L][K] < INF:
            print(DP[L][K])
        else:
            print(-1)

    return 0
                            
if __name__ == "__main__":
    solve() 