import sys
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product, accumulate
from heapq import heapify, heappop, heappush
from functools import lru_cache, total_ordering
from math import gcd, lcm, isqrt
import bisect
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**6)
try:  # PyPy で深い再帰を速くする
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')
except ModuleNotFoundError:
    pass

def input(): return sys.stdin.readline().rstrip()
def II(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

INF = 1 << 60
DIR4 = ((1, 0), (-1, 0), (0, 1), (0, -1))
DIR8 = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
# 英小文字 <-> 数字:  ord(c) - 97 / chr(i + 97)   (大文字は 65)
# 累乗の余り: pow(base, exp, mod)   逆元: pow(x, -1, mod)


def floor_sum(n, m, a, b):
    """Σ_{i=0}^{n-1} floor((a*i + b) / m)   (n >= 0, m >= 1, a, b は負でも可)"""
    ans = 0
    if a < 0 or a >= m:
        ans += n * (n - 1) // 2 * (a // m); a %= m
    if b < 0 or b >= m:
        ans += n * (b // m); b %= m
    while True:
        if a >= m:
            ans += n * (n - 1) // 2 * (a // m); a %= m
        if b >= m:
            ans += n * (b // m); b %= m
        y_max = a * n + b
        if y_max < m: break
        n, b = divmod(y_max, m)
        m, a = a, m
    return ans


class Combination:
    """階乗テーブルによる nCr など (mod は素数、size < mod であること)"""
    def __init__(self, size: int, mod: int):
        self.size = size
        self.mod = mod
        fact = [1] * (size + 1)
        for i in range(1, size + 1):
            fact[i] = fact[i - 1] * i % mod
        inv = [1] * (size + 1)
        inv[size] = pow(fact[size], -1, mod)
        for i in range(size, 0, -1):
            inv[i - 1] = inv[i] * i % mod
        self.fact = fact
        self.inv = inv

    def comb(self, n: int, r: int) -> int:
        """nCr"""
        if r < 0 or n < r or n < 0: return 0
        return self.fact[n] * self.inv[n - r] % self.mod * self.inv[r] % self.mod

    def perm(self, n: int, r: int) -> int:
        """nPr"""
        if r < 0 or n < r or n < 0: return 0
        return self.fact[n] * self.inv[n - r] % self.mod

    def homo(self, n: int, r: int) -> int:
        """nHr (重複組合せ) = (n+r-1)Cr"""
        if n == 0 and r == 0: return 1
        return self.comb(n + r - 1, r)


class UFT:
    """Union-Find (union by size + 経路圧縮)"""
    __slots__ = ("n", "p", "count")

    def __init__(self, N: int):
        self.n = N
        self.p = [-1] * N   # 根なら -(サイズ)、それ以外は親
        self.count = N      # 連結成分の数

    def find(self, a: int) -> int:
        p = self.p
        r = a
        while p[r] >= 0: r = p[r]
        while p[a] >= 0:
            p[a], a = r, p[a]
        return r

    def unite(self, a: int, b: int) -> bool:
        """併合したら True、すでに同じ成分なら False"""
        a = self.find(a); b = self.find(b)
        if a == b: return False
        p = self.p
        if p[a] > p[b]: a, b = b, a
        p[a] += p[b]
        p[b] = a
        self.count -= 1
        return True

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def size(self, a: int) -> int:
        return -self.p[self.find(a)]

    def groups(self) -> list:
        g = defaultdict(list)
        for i in range(self.n): g[self.find(i)].append(i)
        return list(g.values())


@total_ordering
class Fraction:
    """傾き y/x を誤差なしで扱う。約分・符号正規化済みなので set/dict のキーにできる。
    x = 0 は +∞ (垂直) 扱い。(0, 0) は不可。
    """
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        assert x != 0 or y != 0, "Fraction(0, 0) is undefined"
        g = gcd(x, y)
        x //= g; y //= g
        if x < 0 or (x == 0 and y < 0): x, y = -x, -y
        self.x = x
        self.y = y

    def getCoordinate(self):
        return (self.x, self.y)

    def __lt__(self, other):
        return self.y * other.x < self.x * other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"{self.y}/{self.x}"


class Grid:
    def __init__(self, H: int, W: int):
        self.H = H
        self.W = W

    def isInside(self, h: int, w: int) -> bool:
        return 0 <= h < self.H and 0 <= w < self.W

    def neighbors(self, h: int, w: int, dirs=DIR4):
        """(h, w) の隣接マスのうち範囲内のものを列挙"""
        H = self.H; W = self.W
        for dh, dw in dirs:
            nh = h + dh; nw = w + dw
            if 0 <= nh < H and 0 <= nw < W:
                yield nh, nw


class SegTree:
    """非再帰セグメント木（0-indexed, 区間は半開 [l, r)）
    op: 結合的な二項演算, e: 単位元（op(e, x) == x）
    """
    __slots__ = ("n", "size", "op", "e", "d")

    def __init__(self, init: int | list, op, e):
        # init: 初期値のリスト、または要素数 (int)
        if isinstance(init, int):
            init = [e] * init
        self.n = n = len(init)
        self.op = op
        self.e = e
        size = 1
        while size < n: size <<= 1
        self.size = size
        d = [e] * (2 * size)
        d[size:size + n] = init
        for i in range(size - 1, 0, -1):
            d[i] = op(d[2 * i], d[2 * i + 1])
        self.d = d

    def set(self, p, x):
        """A[p] = x"""
        d = self.d; op = self.op
        p += self.size
        d[p] = x
        p >>= 1
        while p:
            d[p] = op(d[2 * p], d[2 * p + 1])
            p >>= 1

    def get(self, p):
        """A[p]"""
        return self.d[p + self.size]

    def prod(self, l, r):
        """op(A[l], ..., A[r-1])。l >= r なら e"""
        d = self.d; op = self.op
        sml = smr = self.e
        l += self.size; r += self.size
        while l < r:
            if l & 1:
                sml = op(sml, d[l]); l += 1
            if r & 1:
                r -= 1; smr = op(d[r], smr)
            l >>= 1; r >>= 1
        return op(sml, smr)

    def all_prod(self):
        return self.d[1]


def solve():
    mod = 998244353
    N, Q = MI()
    S = [[] for _ in range(N+1)]
    for _ in range(Q):
        l, r, x = MI()
        l -= 1
        S[l].append(x)
        S[r].append(-x)

    CS = dict()
    ans = [0] * N
    for i, l in enumerate(S[:N]):
        for key in l:
            if key > 0:
                if key not in CS.keys():
                    CS[key] = 0
                CS[key] += 1
            else:
                key *= -1
                CS[key] -= 1
                if CS[key] <= 0:
                    del CS[key]
        ans[i] = len(CS.keys())
    print(*ans)      
    
    return 0

if __name__ == "__main__":
    solve()