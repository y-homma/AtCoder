import sys
# from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
# sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    N, K, M = map(int, input().split())
    C = [tuple(map(int, input().split())) for _ in range(N)]
    MV = dict()
    NMV = []
    for jw in C:
        c, v = jw
        if c not in MV:
            MV[c] = v
        elif v > MV[c]:
            NMV.append((MV[c], c))
            MV[c] = v
        else:
            NMV.append((v, c))
    # print(MV)
    MVL = []
    for k, v in MV.items():
        MVL.append((v, k))
    MVL.sort(reverse=True)
    Lest = K - M
    ans = 0
    for i in range(M):
        ans += MVL[i][0]
    for i in range(M, len(MVL)):
        NMV.append((MVL[i][0], MVL[i][1]))
    NMV.sort(reverse=True)
    # print(NMV)
    idx = 0
    while Lest > 0:
        ans += NMV[idx][0]
        Lest -= 1
        idx += 1
    print(ans)

    return 0
                            
if __name__ == "__main__":
    solve() 