import sys
from collections import deque
from itertools import permutations
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

    def isConnect(self, a, b):
        return self.find(a) == self.find(b)

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

class Grid:
    def __init__(self, H: int, W: int):
        self.H = H
        self.W = W

    def isInside(self, h, w):
        return 0 <= h < self.H and 0 <= w < self.W

def modPow(base, exp, mod):
    if exp == 0: return 1
    elif exp == 1: return base % mod
    half = modPow(base, exp >> 1, mod)
    if exp % 2 == 0:
        return (half * half) % mod
    else:
        return (half * half * base) % mod

class SegTree():
    def __init__(self, N: int, initValue: list, compare, defaultValue = None):
        self.size = 1
        while self.size < N: self.size <<= 1
        self.listSize = N
        self.compare = compare
        self.tree = [defaultValue] * (2 * self.size - 1)
        for i in range(N):
            self.tree[self.size + i - 1] = initValue[i]
        self.bulkUpdate()
        self.defaultValue = defaultValue

    def bulkUpdate(self):
        for i in reversed(range(self.size - 1)):
            self.tree[i] = self.compare(self.tree[2*i+1], self.tree[2*i+2])

    def update(self, value, position):
        idx = self.size - 1 + position
        self.tree[idx] = value
        while idx > 0:
            pi = (idx - 1) >> 1
            self.tree[pi] = self.compare(self.tree[2*pi+1], self.tree[2*pi+2])
            idx = pi

    def search(self, left, right): #[left, right)
        return self._search(left, right, 0, self.listSize, 0)

    def _search(self, left, right, lb, hb, pos):
        if right <= lb or hb <= left: return self.defaultValue
        if left <= lb and hb <= right: return self.tree[pos]
        else:
            lh = self._search(left, right, lb, (lb + hb) >> 1, 2 * pos + 1)
            rh = self._search(left, right, (lb + hb) >> 1, hb, 2 * pos + 2)
            return self.compare(lh, rh)


def solve():
    input = sys.stdin.readline 
    mod = 998244353
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    IP = [(p, i) for i, p in enumerate(P)]
    S = SegTree(N, IP, compare=lambda a, b: min(a, b), defaultValue=(N+1, N))
    L = SegTree(N, IP, compare=lambda a, b: max(a, b), defaultValue=(-1, N))
    for _ in range(M):
        l, r = map(int, input().split())
        l -= 1
        si = S.search(l, r)
        li = L.search(l, r)
        print(f"Si, Li = {(si, li)}")
        si = si[1]
        li = li[1]
        ps = P[si]
        pl = P[li]
        P[si] = pl
        P[li] = ps
        S.update((pl, si), si)
        S.update((ps, li), li)
        L.update((ps, li), li)
        L.update((pl, si), si)

        print(S.tree)

    print(*P)
        
    return 0
                            
if __name__ == "__main__":
    solve() 