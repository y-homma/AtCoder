import sys
from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
sys.setrecursionlimit(10**6)

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
    E = [[] for _ in range(N)]
    G = UFT(N)
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
        if G.find(u-1) != G.find(v-1):
            G.unite(u-1, v-1)
    
    Parents = set()
    Col = [-1] * N
    PG = dict()
    for i in range(N):
        if Col[i] == -1:
            # 2部グラフの作成
            parent = G.find(i)
            Parents.add(parent)
            PG[parent] = [set(), set()] # 0, 1に塗り分けた頂点
            Q = deque()
            Q.append((parent, 0))
            while len(Q) > 0:
                ci, cc = Q.popleft()
                if Col[ci] == -1:
                    Col[ci] = cc
                    nc = (cc + 1) % 2
                    PG[parent][cc].add(ci)
                    for ni in E[ci]:
                        if Col[ni] > -1:
                            if Col[ni] != nc:
                                print(0)
                                return 0
                        else:
                            Q.append((ni, nc))
                else:
                    if Col[ci] != cc:
                        print(0)
                        return 0
    PSize = {key: len(value[0]) + len(value[1]) for key, value in PG.items()}
    ans = 0
    for i in range(N):
        total = 0
        parent = G.find(i)
        # 同じグループに所属するもの
        col = Col[i]
        ncol = (col + 1) % 2
        total += len(PG[parent][ncol])
        for edge in E[i]:
            if edge in PG[parent][ncol]: 
                total -= 1
        # 別のグループに所属するもの
        total += N - PSize[parent]
        ans += total
        # print(f"For {i}: Pair {total}")
    print(ans // 2)

    return 0 
  
if __name__ == "__main__":
    solve() 