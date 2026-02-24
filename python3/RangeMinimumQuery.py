class RMQ: #range minimum query
    def __init__(self, N, V): #create segment tree with initial value V
        d, k = 1, 0
        while d < N:
            d <<= 1
            k += 1
        self.tree = [V for _ in range(2 * d - 1)]
        self.size = d
    
    def update(self, i, a): #update cell i by value a
        now = self.size - 1 + i 
        self.tree[now] = a
        while now > 0:
            now = (now - 1) // 2
            self.tree[now] = min(self.tree[2 * now + 1], self.tree[2 * now + 2])
        #print(self.tree)

    def search(self, lower, higher, lbound, hbound, pos): #search minimum value of [lower, higher) init: lbound = 0, hbound = self.size, pos = 0
        if higher <= lbound or hbound <= lower: return float("INF")
        if lower <= lbound and hbound <= higher: return self.tree[pos]
        else:
            left = self.search(lower, higher, lbound, (lbound + hbound) // 2, 2 * pos + 1)
            right = self.search(lower, higher, (lbound + hbound) // 2, hbound, 2 * pos + 2)
            return min(left, right)
