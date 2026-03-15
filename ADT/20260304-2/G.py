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
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    As = set(A)
    Acounts = {a: 0 for a in As}
    for a in A:
        Acounts[a] += 1
    Edge = {a: [] for a in As}
    for a in As:
        if (a + 1) % M in As:
            Edge[a].append((a + 1) % M)
            Edge[(a + 1) % M].append(a)
    
    visited = {a : False for a in As}
    q = deque()
    total = sum(A)
    Ans = total + 1
    for a in As:
        if not visited[a]:
            q.append(a)
            subT = 0
            while len(q) > 0:
                current = q.popleft()
                if not visited[current]:
                    visited[current] = True
                    subT += Acounts[current] * current
                    for ne in Edge[current]:
                        if not visited[ne]:
                            q.append(ne)
            Ans = min(Ans, total - subT)
    print(Ans)
    return 0

if __name__ == "__main__":
    solve()
