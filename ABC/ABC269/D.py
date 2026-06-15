import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from itertools import permutations

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
    G = [tuple(map(int, input().split())) for _ in range(N)]
    UT = UFT(N)
    diff = [
        (-1, -1),
        (-1, 0),
        (0, -1),
        (0, 1),
        (1, 0),
        (1, 1)
    ]
    for i in range(N-1):
        xi, yi = G[i]
        for j in range(i+1, N):
            xj, yj = G[j]
            dij = (xi - xj, yi - yj)
            if dij in diff:
                pi = UT.find(i)
                pj = UT.find(j)
                if pi != pj:
                    UT.unite(i, j)
                # print(f"Same: {i} & {j}")
    parents = set()
    for i in range(N):
        pi = UT.find(i)
        parents.add(pi)
    print(len(parents))

    return 0
  
if __name__ == "__main__":
    solve()