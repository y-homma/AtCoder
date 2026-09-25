import sys
from collections import deque
# from itertools import permutations
from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0] * N
    for i in range(1, N): C[i] = B[i-1] - C[i-1]
    D = [C[i] - A[i] for i in range(N)]

    S = []
    for i in range(N):
        S.append((D[i] * (-1) ** ((i+1) % 2)) % M)
    S.sort()
    base = 0
    DD = []
    for i, d in enumerate(D):
        add = d % M
        base += add
        if i % 2 == 0: DD.append((M - add - 1, i)) # 加算(切り替わりまでの猶予)
        else: DD.append((add, i)) # 減算　
    DD.sort()
    Q = deque(DD)
    
    ans = base
    pre = base
    for i in range(N):
        ds = S[i]
        if i > 0: ds -= S[i-1]
        count = pre
        if N % 2 == 1:
            count += ds
        while len(Q) > 0:
            d, idx = Q.popleft()
            if d < S[i]:
                if idx % 2 == 0: count -= M # M-1 -> 0
                else: count += M # 0 -> M-1
            else:
                Q.appendleft((d, idx))
                break
        ans = min(ans, count)
        pre = count
    print(ans)

    # print(C)
    # print(D)
    # print(S)
    # print(DD)
    return 0
                            
if __name__ == "__main__":
    solve() 