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
    N_str = input().strip("\n")
    Sum = [45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    mod = 998244353
    for i in range(1, 18):
        order = pow(10, i)
        max = pow(10, i+1) - 1
        num = max - order + 1
        Sum[i] = (((num * (order + max)) // 2) - (order - 1) * num) % mod

    lenN = len(N_str)
    N = int(N_str)
    base = sum(Sum[:lenN-1]) % mod
    order = pow(10, lenN-1)
    num = N - order + 1
    add = (num * (order + N) // 2 - (order - 1) * num) % mod
    print((base + add) % mod)

    return 0
  
if __name__ == "__main__":
    solve()