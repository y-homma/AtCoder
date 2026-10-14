INF = 1 << 60


class SquareDiv:
    """平方分割による区間 max（0-indexed, 区間は半開 [l, r)）
    1 点更新 O(√N)、区間 max O(√N)。改造（区間加算など）のベースとして使う
    """

    def __init__(self, init: int | list, e=-INF):
        # init: 初期値のリスト、または要素数 (int, 全部 e)
        if isinstance(init, int):
            init = [e] * init
        self.n = n = len(init)
        self.e = e
        b = 1
        while b * b < n: b += 1
        self.b = b                        # ブロックの大きさ
        self.a = list(init)
        self.block = [max(self.a[i:i + b], default=e) for i in range(0, n, b)] or [e]

    def set(self, i: int, v):
        """A[i] = v"""
        self.a[i] = v
        k = i // self.b
        self.block[k] = max(self.a[k * self.b:(k + 1) * self.b])

    def get(self, i: int):
        return self.a[i]

    def max(self, l: int, r: int):
        """max(A[l], ..., A[r-1])。l >= r なら e"""
        a, b, block = self.a, self.b, self.block
        res = self.e
        while l < r and l % b:
            if a[l] > res: res = a[l]
            l += 1
        while l + b <= r:
            if block[l // b] > res: res = block[l // b]
            l += b
        while l < r:
            if a[l] > res: res = a[l]
            l += 1
        return res
