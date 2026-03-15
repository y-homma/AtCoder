import sys
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

    N, M = map(int, input().split())
    E = [None for i in range(M)]
    for i in range(M):
        a, b, c = map(int, input().split())
        E[i] = (c, a-1, b-1)
    E.sort(reverse=False)

    parent = UFT(N)
    point = 0
    for i, e in enumerate(E):
        c, a, b = e
        if parent.find(a) != parent.find(b):
            parent.unite(a, b)
        else:
            if c > 0:
                point += c
    print(point)

    return 0

if __name__ == "__main__":
    solve()
