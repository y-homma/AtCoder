import sys

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
    INF = 10 ** 25
    mod = 998244353
    N, M, S = map(int, input().split()) 
    CNS = Combination(N + S, mod)
    CN = Combination(N, mod)
    
    ans = 0
    for i in range(S + 1):
        if (M + 1) * i > S: break
        CE = CN.comb(i) * pow(-1, i % 2)
        j = S - (M + 1) * i
        # if N < j: continue
        CER = CNS.combNR(N + j - 1, N - 1)
        ans += (CE * CER) % mod
        ans %= mod
        # print(str(i) + " " + str(j) + " " + str(CE) + " " + str(CER))
    print(ans)

    return 0
  
if __name__ == "__main__":
    solve()