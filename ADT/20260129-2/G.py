import sys
from collections import deque

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
    H, W = map(int, input().split())
    A = [input().strip("\n") for _ in range(H)]
    S = (-1, -1)
    T = (-1, -1)
    for h in range(H):
        for w in range(W):
            if A[h][w] == "S": S = (h, w)
            if A[h][w] == "T": T = (h, w)   

    N = int(input())
    drinks = []
    energy = [[-1 for j in range(W)] for i in range(H)]
    edges = [set() for i in range(N)]

    for i in range(N):
        r, c, e = map(int, input().split())
        if r == T[0] + 1 and c == T[1] + 1: 
            edges[i].add(N)
        drinks.append((r-1, c-1, e))
        energy[r-1][c-1] = i
    
    q = deque()
    diff = (-1, 0, 1, 0, -1)
    for i, d in enumerate(drinks):
        limit = d[2]
        visited = [[False for j in range(W)] for _ in range(H)]
        q.append((d[0], d[1], 0))
        while len(q) > 0:
            ch, cw, dist = q.popleft()
            if not visited[ch][cw]:
                if dist <= limit:
                    visited[ch][cw] == True
                    if energy[ch][cw] > -1:
                        edges[i].add(energy[ch][cw])
                    if ch == T[0] and cw == T[1]:
                        edges[i].add(N)
                    if dist == limit:
                        continue
                    for di in range(4):
                        nh = ch + diff[di]
                        nw = cw + diff[di + 1]
                        if nh < 0 or nh >= H or nw < 0 or nw >= W:
                            continue
                        elif not visited[nh][nw] and A[nh][nw] != "#":
                            q.append((nh, nw, dist + 1))
    
    if energy[S[0]][S[1]] == -1:
        print("No")
    else:
        visited = [False for i in range(N + 1)]
        q = deque()
        q.append(energy[S[0]][S[1]])
        while len(q) > 0:
            ci = q.popleft()
            if not visited[ci]:
                visited[ci] = True
                if ci == N: break
                for ni in edges[ci]:
                    if not visited[ni]: q.append(ni)
        print("Yes" if visited[N] else "No")
    return 0
  
if __name__ == "__main__":
    solve()