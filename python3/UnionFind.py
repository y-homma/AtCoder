from collections import defaultdict


class UFT:
    """Union-Find (union by size + 経路圧縮)"""
    __slots__ = ("n", "p", "count")

    def __init__(self, N: int):
        self.n = N
        self.p = [-1] * N   # 根なら -(サイズ)、それ以外は親
        self.count = N      # 連結成分の数

    def find(self, a: int) -> int:
        p = self.p
        r = a
        while p[r] >= 0: r = p[r]
        while p[a] >= 0:
            p[a], a = r, p[a]
        return r

    def unite(self, a: int, b: int) -> bool:
        """併合したら True、すでに同じ成分なら False"""
        a = self.find(a); b = self.find(b)
        if a == b: return False
        p = self.p
        if p[a] > p[b]: a, b = b, a
        p[a] += p[b]
        p[b] = a
        self.count -= 1
        return True

    def same(self, a: int, b: int) -> bool:
        return self.find(a) == self.find(b)

    def size(self, a: int) -> int:
        return -self.p[self.find(a)]

    def groups(self) -> list:
        g = defaultdict(list)
        for i in range(self.n): g[self.find(i)].append(i)
        return list(g.values())
