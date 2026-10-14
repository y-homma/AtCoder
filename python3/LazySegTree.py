class LazySegTree:
    """遅延セグメント木（非再帰, 0-indexed, 区間は半開 [l, r)）
    op(a, b)         : 値の結合（結合的）, e: op の単位元
    mapping(f, x)    : 作用 f を値 x に適用した結果
    composition(f, g): 「g の後に f」を 1 つの作用にまとめたもの
    id_              : 何もしない作用（mapping(id_, x) == x）
    各操作 O(log N)。使用例は下の make_* を参照。
    """
    __slots__ = ("n", "size", "log", "op", "e", "mapping", "composition", "id", "d", "lz")

    def __init__(self, init: int | list, op, e, mapping, composition, id_):
        # init: 初期値のリスト、または要素数 (int)
        if isinstance(init, int):
            init = [e] * init
        self.n = n = len(init)
        self.op = op; self.e = e
        self.mapping = mapping; self.composition = composition; self.id = id_
        log = 0
        while (1 << log) < n: log += 1
        self.log = log
        self.size = size = 1 << log
        self.d = [e] * (2 * size)
        self.lz = [id_] * size
        self.d[size:size + n] = init
        for i in range(size - 1, 0, -1): self._update(i)

    def _update(self, k):
        self.d[k] = self.op(self.d[2 * k], self.d[2 * k + 1])

    def _apply_at(self, k, f):
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size: self.lz[k] = self.composition(f, self.lz[k])

    def _push(self, k):
        f = self.lz[k]
        if f is self.id or f == self.id: return
        self._apply_at(2 * k, f)
        self._apply_at(2 * k + 1, f)
        self.lz[k] = self.id

    def set(self, p, x):
        """A[p] = x"""
        p += self.size
        for i in range(self.log, 0, -1): self._push(p >> i)
        self.d[p] = x
        for i in range(1, self.log + 1): self._update(p >> i)

    def get(self, p):
        """A[p]"""
        p += self.size
        for i in range(self.log, 0, -1): self._push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        """op(A[l], ..., A[r-1])。l >= r なら e"""
        if l >= r: return self.e
        l += self.size; r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self._push(l >> i)
            if ((r >> i) << i) != r: self._push((r - 1) >> i)
        op = self.op; d = self.d
        sml = smr = self.e
        while l < r:
            if l & 1: sml = op(sml, d[l]); l += 1
            if r & 1: r -= 1; smr = op(d[r], smr)
            l >>= 1; r >>= 1
        return op(sml, smr)

    def all_prod(self):
        return self.d[1]

    def apply(self, l, r, f):
        """A[l], ..., A[r-1] に作用 f を適用"""
        if l >= r: return
        l += self.size; r += self.size
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l: self._push(l >> i)
            if ((r >> i) << i) != r: self._push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1: self._apply_at(l, f); l += 1
            if r & 1: r -= 1; self._apply_at(r, f)
            l >>= 1; r >>= 1
        l, r = l2, r2
        for i in range(1, self.log + 1):
            if ((l >> i) << i) != l: self._update(l >> i)
            if ((r >> i) << i) != r: self._update((r - 1) >> i)


# ---- よく使う組み合わせ ----
INF = 1 << 60
_NONE = None  # 代入系の「作用なし」


def make_assign_min(init):
    """区間代入・区間 min"""
    return LazySegTree(init, min, INF,
                       lambda f, x: x if f is None else f,
                       lambda f, g: g if f is None else f, _NONE)


def make_assign_max(init):
    """区間代入・区間 max"""
    return LazySegTree(init, max, -INF,
                       lambda f, x: x if f is None else f,
                       lambda f, g: g if f is None else f, _NONE)


def make_add_min(init):
    """区間加算・区間 min"""
    return LazySegTree(init, min, INF, lambda f, x: x + f, lambda f, g: f + g, 0)


def make_add_max(init):
    """区間加算・区間 max"""
    return LazySegTree(init, max, -INF, lambda f, x: x + f, lambda f, g: f + g, 0)


def make_add_sum(init):
    """区間加算・区間和。値は (和, 区間長) のタプルで持つ。和は prod(l, r)[0]"""
    if isinstance(init, int): init = [0] * init
    return LazySegTree([(a, 1) for a in init],
                       lambda a, b: (a[0] + b[0], a[1] + b[1]), (0, 0),
                       lambda f, x: (x[0] + f * x[1], x[1]),
                       lambda f, g: f + g, 0)


def make_assign_sum(init):
    """区間代入・区間和。値は (和, 区間長) のタプル。和は prod(l, r)[0]"""
    if isinstance(init, int): init = [0] * init
    return LazySegTree([(a, 1) for a in init],
                       lambda a, b: (a[0] + b[0], a[1] + b[1]), (0, 0),
                       lambda f, x: x if f is None else (f * x[1], x[1]),
                       lambda f, g: g if f is None else f, _NONE)
