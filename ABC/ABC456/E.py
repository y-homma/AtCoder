import sys
from collections import deque
import heapq
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

def solve():
    input = sys.stdin.readline 
    T = int(input())
    ans = ["No" for _ in range(T)]
    for t in range(T):
        N, M = map(int, input().split())
        E =[[] for _ in range(N)]
        for i in range(M):
            u, v = map(int, input().split())
            E[u-1].append(v-1)
            E[v-1].append(u-1)

        W = int(input())
        WN = [[] for _ in range(W)]
        WE = [[[] for n in range(N)] for _ in range(W)]

        S = [input().strip("\n") for _ in range(N)]
        for i, s in enumerate(S):
            for j in range(W):
                if s[j] == "o":
                    WN[j].append(i)
        for i, e in enumerate(E):
            ns = S[i]
            for ne in e:
                s = S[ne]
                for w in range(W):
                    if ns[w] == "o" and s[(w+1)%W] == "o":
                        WE[w][i].append(ne)
        
        
        def dfs(w, n, VD, FD):
            cycle = False
            VD[(w, n)] = True
            nd = (w+1)%W
            nes = WE[w][n]
            if S[n][nd] == "o":
                nes.append(n)
            
            for ne in nes:
                if not VD[(nd, ne)]:
                    cycle |= dfs(nd, ne, VD, FD)
                elif not FD[(nd, ne)]:
                    cycle = True
            FD[(w, n)] = True
            return cycle

        VD = {}
        FD = {}
        for w, nodes in enumerate(WN):
            for n in nodes:
                VD[(w, n)] = False
                FD[(w, n)] = False
        
        for n in WN[0]:
            if not VD[(0, n)]:
                if dfs(0, n, VD, FD):
                    ans[t] = "Yes"
                    break
        else:
            ans[t] = "No"

    
    print(*ans, sep="\n")


    return 0
  
if __name__ == "__main__":
    solve()