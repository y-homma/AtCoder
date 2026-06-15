import sys
# from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict

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

def findIndex(n, Arr):
    left = -1
    right = len(Arr)
    while right - left > 1:
        mid = (left + right) >> 1
        if n < Arr[mid]:
            right = mid
        else:
            left = mid
    return left  

def solve():
    input = sys.stdin.readline 
    H, W, rs, cs = map(int, input().split())
    N = int(input())
    DR = dict()
    DC = dict()
    for _ in range(N):
        r, c = map(int, input().split())
        if r not in DR: DR[r] = []
        DR[r].append(c)
        if c not in DC: DC[c] = []
        DC[c].append(r)
    for key in DR.keys():
        DR[key].sort()
    for key in DC.keys():
        DC[key].sort()
    
    Q = int(input())
    ans = [None] * Q
    ci, cj = rs, cs
    for q in range(Q):
        d, l = map(str, input().strip("\n").split())
        l = int(l)
        if d == "L" or d == "R":
            if ci not in DR: DR[ci] = []
            idx = findIndex(cj, DR[ci])
            if d == "L":
                if len(DR[ci]) == 0 or idx == -1:
                    cj = max(1, cj - l)
                else:
                    cj = max(DR[ci][idx] + 1, cj - l)
            else:
                # print(f"Right {l}, DR: {DR[ci]}, idx: {idx}, cj: {cj}")
                if idx >= len(DR[ci]) - 1:
                    cj = min(W, cj + l)
                else:
                    cj = min(DR[ci][idx+1] - 1, cj + l)
        else:
            if cj not in DC: DC[cj] = []
            idx = findIndex(ci, DC[cj])
            if d == "U":
                if len(DC[cj]) == 0 or idx == -1:
                    ci = max(1, ci - l)
                else:
                    ci = max(DC[cj][idx] + 1, ci - l)
            else:
                if idx >= len(DC[cj]) - 1:
                    ci = min(H, ci + l)
                else:
                    ci = min(DC[cj][idx+1] - 1, ci + l)
        ans[q] = (ci, cj)
    for a in ans:
        print(*a)


    return 0
  
if __name__ == "__main__":
    solve() 