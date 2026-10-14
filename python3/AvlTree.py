class _Node:
    __slots__ = ("key", "value", "height", "left", "right")

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1  # このノードを根とする部分木の高さ
        self.left = None
        self.right = None


def _h(n): return 0 if n is None else n.height


def _update(n): n.height = 1 + max(_h(n.left), _h(n.right))


def _rotate_left(n):
    r = n.right
    n.right = r.left
    r.left = n
    _update(n); _update(r)
    return r


def _rotate_right(n):
    l = n.left
    n.left = l.right
    l.right = n
    _update(n); _update(l)
    return l


def _balance(n):
    _update(n)
    b = _h(n.left) - _h(n.right)  # 左が高いと正
    if b > 1:
        if _h(n.left.left) < _h(n.left.right): n.left = _rotate_left(n.left)
        return _rotate_right(n)
    if b < -1:
        if _h(n.right.right) < _h(n.right.left): n.right = _rotate_right(n.right)
        return _rotate_left(n)
    return n


class AVLTree:
    """AVL 木による順序付き map（キーは比較可能なら何でも可）
    insert / delete / get / lower_bound などは各 O(log N)。
    """

    def __init__(self):
        self.root = None
        self.n = 0

    def __len__(self): return self.n

    def __contains__(self, key): return self._find(key) is not None

    def _find(self, key):
        t = self.root
        while t:
            if key < t.key: t = t.left
            elif t.key < key: t = t.right
            else: return t
        return None

    def get(self, key, default=None):
        """key の値。無ければ default"""
        t = self._find(key)
        return default if t is None else t.value

    def insert(self, key, value=None):
        """key に value を設定（既にあれば上書き）"""
        self.root = self._insert(self.root, key, value)

    def _insert(self, t, key, value):
        if t is None:
            self.n += 1
            return _Node(key, value)
        if key < t.key: t.left = self._insert(t.left, key, value)
        elif t.key < key: t.right = self._insert(t.right, key, value)
        else:
            t.value = value
            return t
        return _balance(t)

    def delete(self, key) -> bool:
        """key を削除。削除したら True"""
        n = self.n
        self.root = self._delete(self.root, key)
        return self.n != n

    def _delete(self, t, key):
        if t is None: return None
        if key < t.key: t.left = self._delete(t.left, key)
        elif t.key < key: t.right = self._delete(t.right, key)
        else:
            self.n -= 1
            if t.left is None: return t.right
            if t.right is None: return t.left
            m = t.right  # 右部分木の最小ノードで置き換える
            while m.left: m = m.left
            t.key, t.value = m.key, m.value
            self.n += 1  # 下の再帰で 1 引かれる分を戻す
            t.right = self._delete(t.right, m.key)
        return _balance(t)

    def lower_bound(self, key, default=None):
        """key 以上の最小キー。無ければ default"""
        t, res = self.root, default
        while t:
            if key <= t.key: res = t.key; t = t.left
            else: t = t.right
        return res

    def upper_bound(self, key, default=None):
        """key より大きい最小キー。無ければ default"""
        t, res = self.root, default
        while t:
            if key < t.key: res = t.key; t = t.left
            else: t = t.right
        return res

    def prev(self, key, default=None):
        """key 未満の最大キー。無ければ default"""
        t, res = self.root, default
        while t:
            if t.key < key: res = t.key; t = t.right
            else: t = t.left
        return res

    def floor(self, key, default=None):
        """key 以下の最大キー。無ければ default"""
        t, res = self.root, default
        while t:
            if t.key <= key: res = t.key; t = t.right
            else: t = t.left
        return res

    def min(self, default=None):
        t = self.root
        if t is None: return default
        while t.left: t = t.left
        return t.key

    def max(self, default=None):
        t = self.root
        if t is None: return default
        while t.right: t = t.right
        return t.key

    def items(self):
        """(key, value) を昇順に列挙"""
        stack, t = [], self.root
        while stack or t:
            while t:
                stack.append(t); t = t.left
            t = stack.pop()
            yield t.key, t.value
            t = t.right
