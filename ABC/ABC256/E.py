import sys
from collections import deque

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
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    X = [0] * N
    xi = list(map(int, input().split()))
    for i, x in enumerate(xi):
        X[i] = x - 1

    U = UFT(N)
    
    C = list(map(int, input().split()))

    ans = 0
    for i, x in enumerate(xi):
        if U.find(x-1) != U.find(i):
            U.unite(i, x-1)
            continue
        cur = C[i]
        v = i
        fin = False
        while not fin:
            v = X[v]
            cur = min(cur, C[v])
            if v == i:
                fin = True
        ans += cur

    
    print(ans)

    return 0
  
if __name__ == "__main__":
    solve()