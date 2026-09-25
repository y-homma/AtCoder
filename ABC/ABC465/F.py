import sys
# from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
# import bisect
# sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    N = int(input())
    pow10 = [10 ** i for i in range(6)]
    KMAX = 10 ** 6
    S = [0] * KMAX
    SV = [tuple(map(str, input().strip("\n").split())) for _ in range(N)]
    for _, sv in enumerate(SV):
        s, v = sv
        v = int(v)
        sint = int(s)
        S[sint] += v
    for digit in range(6):
        for i in range(KMAX):
            if (i // pow10[digit]) % 10 > 0:
                S[i] += S[i - pow10[digit]]

    Q = int(input())
    Ans = [0] * Q
    for q in range(Q):
        x, y = map(str, input().strip("\n").split())
        isXsmaller = True
        xd = [0] * 6
        yd = [0] * 6
        for d in range(6):
            xd[d] = int(x[d])
            yd[d] = int(y[d])
            if xd[d] > yd[d]:
                isXsmaller = False
                break
        if not isXsmaller:
            Ans[q] = 0
            continue
        
        ans = 0
        for bit in range(1 << 6):
            sidx = 0
            bitCount = 0
            for d in range(6):
                base = pow10[6-d-1]
                if (bit & (1 << d)) > 0:
                    bitCount += 1
                    if xd[d] == 0: 
                        break
                    sidx += (xd[d] - 1) * base
                else:
                    sidx += yd[d] * base
            else:
                if bitCount % 2 == 0:
                    ans += S[sidx]
                else:
                    ans -= S[sidx]
        Ans[q] = ans
    print(*Ans, sep="\n")

    return 0
                            
if __name__ == "__main__":
    solve() 