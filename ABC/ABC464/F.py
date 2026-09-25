import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

class Combination:
    def __init__(self, size: int, mod: int):
        self.size = size
        self.mod = mod
        self.fact = [1] * (size + 1)
        for i in range(1, size + 1):
            self.fact[i] = (self.fact[i-1] * i) % mod
        self.factN = self.fact[size]
        self.revFact = [1] * (size + 1)
        self.revFact[size] = pow(self.factN, -1, mod)
        for i in reversed(range(1, size)):
            self.revFact[i] = (self.revFact[i+1] * (i + 1)) % mod
    
    def comb(self, r: int) -> int:
        if r < 0 or self.size < r: return 0
        return (self.factN * self.revFact[self.size - r] * self.revFact[r]) % self.mod
    
    def combNR(self, N: int, r: int) -> int:
        if N > self.size: return 0
        if r < 0 or N < r: return 0
        return (self.fact[N] * self.revFact[N - r] * self.revFact[r]) % self.mod

def solve():
    input = sys.stdin.readline 
    mod = 998244353
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    C = Combination(N, mod)
    selectK = [pow((N-k)*C.comb(k), -1, mod) for k in range(N)]
    selectK.append(0)
    
    aAll = sum(A) % mod
    LSize = N // 2
    if N > 20: LSize -= 2
    Left = A[:LSize]
    Right = A[LSize:]      
    RSize = len(Right)
    RD = [[] for _ in range(RSize+1)]
    for i in range(pow(2, RSize)):
        K = i
        bc = 0
        total = 0
        for j in range(RSize):
            if K % 2 == 1:
                bc += 1
                total += Right[j]
            K >>= 1
        RD[bc].append(total)
    # print(RD)
    RSum = dict()
    for k in range(RSize+1):
        RD[k].sort()
        sl = len(RD[k])
        s = [0] * sl
        s[0] = RD[k][0] % mod
        for i in range(1, sl):
            s[i] = (s[i-1] + RD[k][i]) % mod
        RSum[k] = s
    
    ans = 0
    for i in range(pow(2, LSize)):
        K = i
        bc = 0
        total = 0
        for j in range(LSize):
            if K % 2 == 1:
                bc += 1
                total += Left[j]
            K >>= 1
        upMost = X - total
        # print(f"K: {i}, bc: {bc}, total: {total}, upMost: {upMost}")

        for rCount in range(RSize + 1):
            rList = RD[rCount]
            idx = bisect.bisect_left(rList, upMost)
            if idx == 0: continue
            rUsedTotal = RSum[rCount][idx - 1]
            patterns = idx
            aAllSub = (aAll * patterns) % mod
            ans += (selectK[bc+rCount] * ((aAllSub - rUsedTotal - total * patterns) % mod)) % mod
            ans %= mod
    print(ans)
                
    return 0
                            
if __name__ == "__main__":
    solve() 