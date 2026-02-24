import sys

class LST(): #遅延セグ木
    def __init__(self, N, V): #create segment tree with initial value V
        self.size = 1
        while self.size < N: self.size <<= 1
        self.tree = [V] * (2 * self.size - 1)
        self.changed = [-1] * (2 * self.size - 1) 

    def eval(self, i, left, right): #遅延評価, [left, right)
        t = self.changed[i]
        if t > -1:
            self.tree[i] = t
            if right - left > 1:
                self.changed[2 * i + 1] = t 
                self.changed[2 * i + 2] = t
            self.changed[i] = -1
    
    def update(self, v, lower, higher, lbound, hbound, pos): #update cell i by value a, pos = 0  
        self.eval(pos, lbound, hbound)    
        if higher <= lbound or hbound <= lower: return
        if lower <= lbound and hbound <= higher: 
            self.tree[pos] = v
            if hbound - lbound > 1: self.changed[2 * pos + 1] = self.changed[2 * pos + 2] = v
        else:
            self.update(v, lower, higher, lbound, (lbound + hbound) // 2, 2 * pos + 1)
            self.update(v, lower, higher, (lbound + hbound) // 2, hbound, 2 * pos + 2)
            self.tree[pos] = min(self.tree[2 * pos + 1], self.tree[2 * pos + 2])

    def search(self, lower, higher, lbound, hbound, pos): #search minimum value of [lower, higher) init: lbound = 0, hbound = self.size, pos = 0
        if higher <= lbound or hbound <= lower: return 2 ** 31 - 1

        self.eval(pos, lbound, hbound)
        if lower <= lbound and hbound <= higher: return self.tree[pos]
        else:
            left = self.search(lower, higher, lbound, (lbound + hbound) // 2, 2 * pos + 1)
            right = self.search(lower, higher, (lbound + hbound) // 2, hbound, 2 * pos + 2)
            return min(left, right)

def solve():
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    Tree = LST(N, 2 ** 31 - 1)
    for _ in range(Q):
        query = [int(j) for j in input().split()]
        if query[0] == 0: Tree.update(query[3], query[1], query[2] + 1, 0, Tree.size, 0)
        else: print(Tree.search(query[1], query[2] + 1, 0, Tree.size, 0))

    return 0

if __name__ == "__main__":
    solve()