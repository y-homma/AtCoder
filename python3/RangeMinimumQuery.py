INF = 1 << 60


class RMQ:
    """区間 min（1 点更新, 0-indexed, 区間は半開 [l, r)）。各 O(log N)
    Template.py の SegTree(init, min, INF) と同じ。min 専用で少し速い
    """
    __slots__ = ("n", "size", "d")

    def __init__(self, init: int | list):
        # init: 初期値のリスト、または要素数 (int, 全部 INF)
        if isinstance(init, int):
            init = [INF] * init
        self.n = n = len(init)
        size = 1
        while size < n: size <<= 1
        self.size = size
        d = [INF] * (2 * size)
        d[size:size + n] = init
        for i in range(size - 1, 0, -1):
            d[i] = d[2 * i] if d[2 * i] < d[2 * i + 1] else d[2 * i + 1]
        self.d = d

    def set(self, p: int, x):
        """A[p] = x"""
        d = self.d
        p += self.size
        d[p] = x
        p >>= 1
        while p:
            d[p] = d[2 * p] if d[2 * p] < d[2 * p + 1] else d[2 * p + 1]
            p >>= 1

    def get(self, p: int):
        return self.d[p + self.size]

    def min(self, l: int, r: int):
        """min(A[l], ..., A[r-1])。l >= r なら INF"""
        d = self.d
        res = INF
        l += self.size; r += self.size
        while l < r:
            if l & 1:
                if d[l] < res: res = d[l]
                l += 1
            if r & 1:
                r -= 1
                if d[r] < res: res = d[r]
            l >>= 1; r >>= 1
        return res
