import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

memo = dict()

def pay(X, i, A):
    if X == 0:
        return 0
    if i == len(A) - 1:
        if X not in memo:
            memo[X] = X // A[i]
        return memo[X]
    if X not in memo:
        fraction = X % A[i+1]
        under = X // A[i+1]
        over = under + 1
        change = A[i+1] - fraction       

        caseLow = pay(under * A[i+1], i+1, A)
        caseOver = pay(over * A[i+1], i+1, A)
        memo[X] = min(fraction // A[i] + caseLow, change // A[i] + caseOver)
    return memo[X]

def solve():
    input = sys.stdin.readline 
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    print(pay(X, 0, A))
    # print(memo)
    return 0
                            
if __name__ == "__main__":
    solve() 