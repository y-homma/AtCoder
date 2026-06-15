import sys
from collections import deque

def findS(L, T):
    low = -1
    high = len(L)
    while high - low > 1:
        mid = (high + low) // 2
        t, i = L[mid]
        if t <= T:
            low = mid
        else:
            high = mid
    return low

def findT(L, S):
    low = -1
    high = len(L)
    while high - low > 1:
        mid = (high + low) // 2
        s, i = L[mid]
        if s < S:
            low = mid
        else:
            high = mid
    return high    

  
def solve():
    input = sys.stdin.readline 
    N, M = map(int, input().split())
    C = [tuple(map(int, input().split())) for _ in range(M)]
    Start = dict()
    End = dict()
    CD = dict()
    for i, c in enumerate(C):
        s, t = c
        if s not in Start: Start[s] = []
        if t not in End: End[t] = []
        if (s, t) not in CD: CD[(s, t)] = []
        Start[s].append((t, i))
        End[t].append((s, i))
        CD[(s, t)].append(i)
    for key in Start.keys():
        Start[key].sort()
    for key in End.keys():
        End[key].sort()

    SM = [N] * (N + 1)
    TM = [0] * (N + 1)

    Q = int(input())
    Ans = ["No"] * Q
    for q in range(Q):
        s, t = map(int, input().split())
        if s not in Start or t not in End:
            Ans[q] = "No"
        elif (s, t) in CD:
            if (len(CD[(s, t)]) > 1):
                Ans[q] = "Yes"
            else:
                # [s+1, t]
                minT = SM[s+1]
                if minT <= t:
                    Ans[q] = "Yes"
                    continue
                # [s, t-1]
                maxS = TM[t-1]
                if maxS >= s:
                    Ans[q] = "Yes"
                    continue
                Ans[q] = "No"
        else:
            si = findS(Start[s], t)
            ti = findT(End[t], s)
            if si == -1 or ti == len(End[t]):
                Ans[q] = "No"
                continue
            st, sindex = Start[s][si]
            ts, tindex = End[t][ti]
            if st < ts or st > t or ts < s:
                Ans[q] = "No"
                continue
            elif sindex != tindex:
                Ans[q] = "Yes"
                continue
                    
    print(*Ans, sep="\n")

    return 0
  
if __name__ == "__main__":
    solve()