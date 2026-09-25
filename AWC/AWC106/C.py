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

def isInside(h, w, H, W):
    return 0 <= h < H and 0 <= w < W

def solve():
    input = sys.stdin.readline 
    N, Q = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
    S = 0
    Ans = []
    INF = 1000000000000
    for _ in range(Q):
        query = list(map(int, input().strip("\n").split()))
        qt = query[0]
        if qt == 1:
            c = query[1] - 1
            P[c][0] *= -1
            P[c][1] *= -1
        elif qt == 2:
            S += query[1]
        else:
            A = query[1] - 1
            B = query[2] - 1
            D = [INF] * N
            Path = [INF] * N
            Q = deque()
            Q.append((A, 0, 1, -1))
            while len(Q) > 0:
                idx, d, pc, parent = Q.popleft()
                if d < D[idx]:
                    D[idx] = d
                    Path[idx] = pc
                    cx, cy = P[idx]
                    if idx == B:
                        break
                    for ne in E[idx]:
                        if ne != parent:
                            nd = d + abs(P[ne][0] - cx) + abs(P[ne][1] - cy)
                            Q.append((ne, nd, pc + 1, idx))
            Ans.append(D[B] + S * Path[B])
    print(*Ans, sep="\n")

               
    return 0
                            
if __name__ == "__main__":
    solve() 