import sys
from collections import deque
import heapq
import itertools

class Alphabet: #Trueなら大文字
    def __init__(self, capitalize):
        self.indexOf = dict() #アルファベットを数字に変換
        self.abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"\
            ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if capitalize: 
            for i in range(26): self.abc[i] = self.abc[i].upper()
        for i, a in enumerate(self.abc): self.indexOf[a] = i

    # 指定したIndexの英文字を取得します
    def get(self, index):
        return self.abc[index]

    # 指定した英文字のインデックスを取得します
    def indexOf(self, chr):
        return self.indexOf[chr]

class Math:
    def __init__(self):
        return

    # Σ0,N-1 floor((A * i + B) / M)を求める
    def floorSum(self, n, m, a, b):
        ans = 0
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m

        y_max = (a * n + b) // m
        x_max = (y_max * m - b)
        if y_max == 0: return ans
        ans += (n - (x_max + a - 1) // a) * y_max
        ans += self.floorSum(y_max, a, m, (a - x_max % a) % a)
        return ans

    # 指定した2数のGCDを取ります
    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while a % b > 0: a, b = b, a % b
        return b

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
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = []
    isPrime = [True] * 100001
    isPrime[0] = False
    isPrime[1] = False
    primes = []
    for i in range(2, 100001):
        if not isPrime[i]: continue
        primes.append(i)
        ci = i * 2
        while ci <= 100001:
            isPrime[i] = False
            ci += i
    
    C = set([i for i in range(1, M+1)])
    for a in A:
        ca = a
        for prime in primes:
            if prime * prime > a: break
            if ca % prime == 0:
                while ca % prime == 0:
                    ca //= prime
                if prime in C:
                    cp = prime
                    while cp <= M:
                        C.discard(cp)
                        cp += prime
        if ca > 1 and ca in C:
            cp = ca
            while cp <= M:
                C.discard(cp)
                cp += ca
    
    
    print(len(C))
    C = sorted(list(C))
    print(*C, sep="\n")

    return 0
  
if __name__ == "__main__":
    solve()