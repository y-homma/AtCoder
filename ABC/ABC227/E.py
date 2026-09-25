import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

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
    def index(self, chr):
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
    
class UFT: #Union-find tree class
    def __init__(self, N): 
        self.tree = [int(i) for i in range(N)] 
        self.rank = [0 for i in range(N)]

    def find(self, a):
        if self.tree[a] == a: return a
        else:
            self.tree[a] = self.find(self.tree[a])
            return self.tree[a]

    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.rank[a] < self.rank[b]: self.tree[a] = b
        else:
            self.tree[b] = a
            if self.rank[a] == self.rank[b]: self.rank[a] += 1

class Fraction:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def getCoordinate(self):
        return (self.x, self.y)
    
    def __lt__(self, other):
        return self.y * other.x < self.x * other.y
    
    def __le__(self, other):
        return self.y * other.x <= self.x * other.y
    
    def __eq__(self, other):
        return self.y * other.x == other.y * self.x

def isInside(h, w, H, W):
    return 0 <= h < H and 0 <= w < W

def solve():
    input = sys.stdin.readline 
    S = input().strip("\n")
    K = int(input())
    L = len(S)
    ec = S.count("E")
    yc = S.count("Y")
    maxMove = min(L * L, K)
    DP = [[[[0 for y in range(yc + 1)] for e in range(ec + 1)] for x in range(maxMove + 1)] for _ in range(L)]
    fK, fE, fY = -1, -1, -1
    for i in range(L):
        if S[i] == "K" and fK == -1:
            fK = i
        if S[i] == "E" and fE == -1:
            fE = i
        if S[i] == "Y" and fY == -1:
            fY = i
    if fK > -1 and fK <= maxMove: DP[0][fK][0][0] = 1
    if fE > -1 and fE <= maxMove: DP[0][fE][1][0] = 1
    if fY > -1 and fY <= maxMove: DP[0][fY][0][1] = 1
    SI = {"K": 0, "E": 1, "Y": 2}

    for i in range(L - 1):
        for k in range(maxMove + 1):
            for e in range(ec + 1):
                for y in range(yc + 1):
                    count = DP[i][k][e][y]
                    if count > 0:
                        LC = [i+1-e-y, e, y]
                        Left = []
                        for j in range(L):
                            li = SI[S[j]]
                            if LC[li] == 0:
                                Left.append(S[j])
                            else:
                                LC[li] -= 1
                        nK, nE, nY = -1, -1, -1
                        for j in range(len(Left)):
                            if Left[j] == "K" and nK == -1: nK = j
                            if Left[j] == "E" and nE == -1: nE = j
                            if Left[j] == "Y" and nY == -1: nY = j
                        if nK > -1 and k+nK <= maxMove: DP[i+1][k+nK][e][y] += count
                        if nE > -1 and k+nE <= maxMove: DP[i+1][k+nE][e+1][y] += count
                        if nY > -1 and k+nY <= maxMove: DP[i+1][k+nY][e][y+1] += count
    
    ans = 0
    for k in range(maxMove + 1):
        ans += DP[L-1][k][ec][yc]
    print(ans)
    # print(DP)
    return 0
                            
if __name__ == "__main__":
    solve() 