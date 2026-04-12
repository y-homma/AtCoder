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
    
def calc(k, n, idx, LS, XC, YC, SC):
    if k == 0:
        return XC[n][idx]
    elif k == 1:
        return YC[n][idx]
    else:
        if n <= LS[k-1]:
            return calc(k-1, n, idx, LS, XC, YC, SC)
        else:
            prevCount = SC[k-1][idx]
            thisCount = calc(k-2, n-LS[k-1], idx, LS, XC, YC, SC)
            return prevCount + thisCount

  
def solve():
    input = sys.stdin.readline 
    X = input().strip("\n")
    Y = input().strip("\n")
    Q = int(input())
    ABC =Alphabet(False)
    maxR = 0
    query = [[] for _ in range(Q)]
    for i in range(Q):
        query[i] = list(map(str, input().split()))
        maxR = max(maxR, int(query[i][1]))
    
    LS = [len(X), len(Y)]
    idx = 2
    while True:
        s0 = LS[idx - 2]
        s1 = LS[idx - 1]
        s = s0 + s1
        LS.append(s)
        idx += 1
        if s >= maxR:
            break
    K = len(LS)
    XC = [[0] * 26 for _ in range(len(X)+1)]
    YC = [[0] * 26 for _ in range(len(Y)+1)]

    for i in range(1, len(X)+1):
        idx = ABC.index(X[i-1])
        XC[i][idx] = 1
        for j in range(26):
            XC[i][j] += XC[i-1][j]

    for i in range(1, len(Y)+1):
        idx = ABC.index(Y[i-1])
        YC[i][idx] = 1
        for j in range(26):
            YC[i][j] += YC[i-1][j]
    
    SC = dict()
    SC[0] = XC[-1]
    SC[1] = YC[-1]
    for i in range(2, K+1):
        s0 = SC[i-2]
        s1 = SC[i-1]
        SC[i] = [s0[j] + s1[j] for j in range(26)]
    ans = [0] * Q
    for i in range(Q):
        l, r, c = query[i]
        idx = ABC.index(c)
        left = calc(K, int(l)-1, idx, LS, XC, YC, SC)
        # print(f"Left {int(l) - 1}: {left}")
        right = calc(K, int(r), idx, LS, XC, YC, SC)
        # print(f"Right {int(r)}: {right}")
        ans[i] = right - left

    print(*ans, sep="\n")
    return 0
  
if __name__ == "__main__":
    solve()