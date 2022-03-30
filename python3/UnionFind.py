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

def debug():
    N, M = map(int, input().split())
    parent = UFT(N)
    for i in range(M):
        x, y, z = map(int, input().split())
        parent.unite(x-1, y-1)
    for i in range(N):
        parent.find(i)

    print(len(set(parent.tree)))
