import sys
from collections import deque
import heapq

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
    def gcd(a, b):
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
    H, W, N = map(int, input().split())
    Q = [None] * N
    HD = dict()
    WD = dict()
    for i in range(N):
        h, w  = map(int, input().split())
        Q[i] = (h, w)
        if h not in HD.keys(): HD[h] = []
        HD[h].append(i)
        if w not in WD.keys(): WD[w] = []
        WD[w].append(i)

    Ans = [None] * N
    CH, CW = H, W
    Fin = set()
    while CH > 0 and CW > 0:
        # print(f"{CH}-{CW}")
        if CH in HD.keys():
            cand = HD[CH]
            for i in cand:
                if i not in Fin:
                    Ans[i] = (H - CH + 1, W - CW + 1)
                    CW -= Q[i][1]
                    Fin.add(i)
            del HD[CH]
        elif CW in WD.keys():
            cand = WD[CW]
            for i in cand:
                if i not in Fin:
                    Ans[i] = (H - CH + 1, W - CW + 1)
                    CH -= Q[i][0]
                    Fin.add(i)
            del WD[CW]
    # print(Ans)
    for ans in Ans:
        print(f"{ans[0]} {ans[1]}")

    return 0
  
if __name__ == "__main__":
    solve()