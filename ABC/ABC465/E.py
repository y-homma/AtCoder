import sys
from collections import deque
# from itertools import permutations
from heapq import heapify, heappop, heappush
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

def isInside(h, w, H, W):
    return 0 <= h < H and 0 <= w < W

def updateBit(curBit, num):
    return curBit | (1 << num)

def countBit(bit):
    count = 0
    base = bit
    for i in range(10):
        count += base % 2
        base >>= 1
    return count

def solve():
    input = sys.stdin.readline 
    N = int(input())
    mod = 998244353
    NS = str(N)
    size = len(NS)
    DP = [[[[0 for isLower in range(2)] for mod3 in range(3)] for useBit in range(2 ** 10)] for _ in range(size)]
    topNum = int(NS[0])
    DP[0][updateBit(0, topNum)][topNum % 3][0] = 1
    DP[0][0][0][1] = 1
    for k in range(1, topNum):
        DP[0][1 << k][k % 3][1] = 1

    for i in range(1, size):
        num = int(NS[i])
        for prevBit in range(2 ** 10):
            for prevMod in range(3):
                baseMod = (prevMod * 10) % 3
                prevTop = DP[i-1][prevBit][prevMod][0]
                prevLow = DP[i-1][prevBit][prevMod][1]
                if prevTop > 0:
                    DP[i][updateBit(prevBit, num)][(baseMod + num) % 3][0] += prevTop
                    for k in range(num):
                        DP[i][updateBit(prevBit, k)][(baseMod + k) % 3][1] += prevTop
                if prevLow > 0:
                    for k in range(10):
                        if k == 0 and prevBit == 0:
                            DP[i][0][baseMod][1] = (DP[i][0][baseMod][1] + prevLow) % mod
                        else:
                            newBit = updateBit(prevBit, k)
                            DP[i][newBit][(baseMod + k) % 3][1] = (DP[i][newBit][(baseMod + k) % 3][1] + prevLow) % mod
    
    ans = 0
    for bit in range(1, 2 ** 10):
        isType3 = countBit(bit) == 3
        isIn3 = (bit & (1 << 3)) > 0
        if isType3 and isIn3:
            continue
        for mod3 in range(3):
            isMult3 = mod3 == 0
            if (isIn3 and isMult3) or (isMult3 and isType3):
                continue
            if not isIn3 and not isType3 and not isMult3:
                continue
            ans = (ans + DP[size-1][bit][mod3][0] + DP[size-1][bit][mod3][1]) % mod

    print(ans)

    return 0
                            
if __name__ == "__main__":
    solve() 