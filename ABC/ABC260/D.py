import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N, K= map(int, input().split())
    P = list(map(int, input().split()))
    S = SortedSet()
    D = defaultdict(list)
    Ans = [-1] * N
    for i, p in enumerate(P):
        si = S.bisect_left(p)
        if si == len(S):
            S.add(p)
        key = S[si]
        l = D[key]
        l.append(p)

        S.discard(S[si])
        S.add(p)
        D[p] = l

        if len(D[p]) == K:
            S.discard(p)
            D.pop(p)
            for item in l:
                Ans[item-1] = i+1
    print(*Ans, sep="\n")

    return 0
  
if __name__ == "__main__":
    solve()