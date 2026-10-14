class BIT:
    """Binary Indexed Tree / Fenwick Tree（0-indexed, 区間は半開 [l, r)）
    1 点加算と区間和が各 O(log N)。
    """
    __slots__ = ("n", "d")

    def __init__(self, n: int):
        self.n = n
        self.d = [0] * (n + 1)  # 内部は 1-indexed

    def add(self, i: int, x):
        """A[i] += x"""
        d = self.d; n = self.n
        i += 1
        while i <= n:
            d[i] += x
            i += i & -i

    def sum(self, r: int):
        """A[0] + ... + A[r-1]"""
        d = self.d
        s = 0
        while r > 0:
            s += d[r]
            r -= r & -r
        return s

    def range_sum(self, l: int, r: int):
        """A[l] + ... + A[r-1]"""
        return self.sum(r) - self.sum(l)

    def lower_bound(self, w):
        """A[0] + ... + A[i] >= w となる最小の i（全要素が非負のとき）。無ければ n"""
        if w <= 0: return 0
        d = self.d; n = self.n
        i = 0
        k = 1 << n.bit_length()
        while k:
            if i + k <= n and d[i + k] < w:
                w -= d[i + k]
                i += k
            k >>= 1
        return i
