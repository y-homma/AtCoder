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
    N = input().strip("\n")
    l = len(N)
    nums = [0 for _ in range(l)]
    for i in range(len(N)):
        nums[i] = int(N[i])
    nums.sort(reverse=True)
    maxM = 0
    for i in range(pow(2, l)):
        tmp = i
        A = 0
        B = 0
        for j in range(l):
            if tmp % 2 == 1:
                A = A * 10 + nums[j]
            else:
                B = B * 10 + nums[j]
            tmp = tmp >> 1
        maxM = max(maxM, A * B)
    print(maxM)

    return 0
  
if __name__ == "__main__":
    solve()