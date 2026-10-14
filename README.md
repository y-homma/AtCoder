# 競技プログラミング

## C++実行(WSL2, Ubuntu24)
```
# 例: ABC/ABC001/A.cpp
$ bd A
$ io -f ./A.out -i in.txt -o out.txt

# ../../../build.sh A
# ../../../io.sh -f ./A.out -i in.txt -o out.txt
```

## Python (`python3/`)

### テンプレート: `Template.py`

新しい問題はこれをコピーして `solve()` に書く。PyPy 前提（`pypyjit` があれば再帰を高速化、無ければ無視）。

| 名前 | 内容 |
| --- | --- |
| `input()` / `II()` / `MI()` / `LI()` | 高速入力 / int 1個 / int の map / int のリスト |
| `INF` | `1 << 60` |
| `DIR4` / `DIR8` | 4方向・8方向の移動 `(dh, dw)` |
| `floor_sum(n, m, a, b)` | Σ_{i=0}^{n-1} ⌊(a·i + b) / m⌋（a, b は負でも可） |
| `Combination(size, mod)` | `comb(n, r)` nCr, `perm(n, r)` nPr, `homo(n, r)` nHr。mod は素数 |
| `UFT(N)` | Union-Find。`find` / `unite`(併合したら True) / `same` / `size` / `groups()` / `count`(連結成分数) |
| `Fraction(x, y)` | 傾き y/x を誤差なしで比較・ハッシュ。x=0 は +∞ 扱い、(0, 0) は不可 |
| `Grid(H, W)` | `isInside(h, w)`、`neighbors(h, w, dirs=DIR4)` で範囲内の隣接マスを列挙 |
| `SegTree(init, op, e)` | 非再帰セグ木。`set(p, x)` / `get(p)` / `prod(l, r)` は半開区間 / `all_prod()` |

```python
seg = SegTree(A, min, INF)           # 区間 min
seg = SegTree(N, lambda a, b: a + b, 0)  # 区間和（要素数 N, 全部 0）
seg.set(3, 10); seg.prod(0, 5)
```

便利メモ（Template.py 内のコメントにもあり）:
- 英小文字 ↔ 数字: `ord(c) - 97` / `chr(i + 97)`（大文字は 65）
- 累乗の余り `pow(b, e, mod)`、逆元 `pow(x, -1, mod)`
- `sortedcontainers` は import をコメントアウトしてある（使う時に外す）

### 単体ライブラリ

必要なファイルの中身をコピーして使う。共通ルール:

- **0-indexed、区間は半開区間 `[l, r)`**（`SegTree` と同じ）
- 標準入力は読まない。関数・クラスとして呼ぶだけ
- 初期値を受け取るクラスは「リスト」か「要素数 (int)」のどちらでも渡せる

| ファイル | 中身 | 主な API | 計算量 |
| --- | --- | --- | --- |
| `AvlTree.py` | AVL 木（順序付き map） | `AVLTree()`、`insert(k, v=None)` / `delete(k)` / `get(k, default)` / `k in T` / `len(T)` / `items()` / `min()` / `max()` | 各 O(log N) |
| | 二分探索 | `lower_bound(k)` k 以上の最小, `upper_bound(k)` k より大きい最小, `floor(k)` k 以下の最大, `prev(k)` k 未満の最大（無ければ `default`=None） | O(log N) |
| `BellmanFord.py` | ベルマンフォード | `dist, neg = bellman_ford(N, edges, s=0)`、`edges = [(u, v, cost), ...]`。到達不能は `INF`、負閉路の影響を受ける頂点は `-INF`、`neg` は負閉路の有無 | O(NM) |
| `BinaryIndexedTree.py` | BIT（Fenwick Tree） | `BIT(n)`、`add(i, x)`、`sum(r)` は [0, r) の和、`range_sum(l, r)`、`lower_bound(w)` 累積和が w 以上になる最小の i（非負のとき） | 各 O(log N) |
| `InversionNumber.py` | 転倒数 | `inversion(A)`。値は任意（座標圧縮する） | O(N log N) |
| `LazySegTree.py` | 遅延セグ木（汎用） | `LazySegTree(init, op, e, mapping, composition, id_)`、`apply(l, r, f)` / `prod(l, r)` / `set(p, x)` / `get(p)` / `all_prod()` | 各 O(log N) |
| | よく使う組み合わせ | `make_assign_min` / `make_assign_max` / `make_add_min` / `make_add_max` / `make_add_sum` / `make_assign_sum`（`*_sum` は値が `(和, 長さ)` のタプル。和は `prod(l, r)[0]`、`set` も `(x, 1)` で渡す） | |
| `LCS.py` | 最長共通部分列 | `LCS(s, t)` で LCS を 1 つ返す（文字列なら文字列、リストならリスト）。長さは `len(...)` | O(\|s\|\|t\|) |
| `LIS.py` | 最長増加部分列の長さ | `LIS(A, strict=True)`。`strict=False` で広義増加 | O(N log N) |
| `MaximumFlow.py` | 最大流（Dinic） | `mf = MaxFlow(N)`、`add_edge(u, v, cap)` → 辺番号、`flow(s, t)`、`get_edge(i)` → (from, to, cap, flow)、`min_cut(s)` で s 側の頂点 | O(V²E)（実用上速い） |
| `RangeMinimumQuery.py` | 区間 min（1 点更新） | `RMQ(init)`、`set(p, x)` / `get(p)` / `min(l, r)`。`SegTree(init, min, INF)` の min 専用版 | 各 O(log N) |
| `SquareDivision.py` | 平方分割（区間 max） | `SquareDiv(init)`、`set(i, v)` / `get(i)` / `max(l, r)`。区間加算などに改造するベース | 各 O(√N) |
| `TopologicalSort.py` | トポロジカルソート | `topological_sort(N, edges)`、`edges = [(u, v), ...]`。閉路があれば `None` | O(N + M) |
| `TopologicalSortCount.py` | トポロジカル順序の数え上げ | `count_topological_sort(N, edges, mod=None)`。N ≲ 20 | O(2^N · N) |
| `UnionFind.py` | Union-Find | `Template.py` の `UFT` と同じもの | ほぼ O(1) |

```python
# 遅延セグ木: 区間加算・区間 min
T = make_add_min([3, 1, 4, 1, 5])
T.apply(1, 4, 10)   # A[1..3] += 10
T.prod(0, 5)        # -> 3  ([3, 11, 14, 11, 5])

# 自分で作る場合（例: 区間アフィン変換 x -> a*x + b・区間和, 値は (和, 長さ)）
T = LazySegTree([(a, 1) for a in A],
                lambda x, y: ((x[0] + y[0]) % mod, x[1] + y[1]), (0, 0),
                lambda f, x: ((f[0] * x[0] + f[1] * x[1]) % mod, x[1]),
                lambda f, g: (f[0] * g[0] % mod, (f[0] * g[1] + f[1]) % mod), (1, 0))

# 最大流
mf = MaxFlow(N)
mf.add_edge(0, 1, 5)
mf.flow(0, N - 1)
```

### 注意

- `AvlTree.py` は再帰（深さ O(log N)）、他は非再帰。
- `LazySegTree.py` の `mapping` / `composition` を自作するときは「`composition(f, g)` は g の後に f」の順番に注意。
- `make_assign_*` は「作用なし」を `None` で表すので、`None` を代入値に使わない。
- `TopologicalSort.py` で辞書順最小の順序が欲しいときは、`deque` を `heapq` に置き換える。

## Java用テンプレート

TODO

## ライセンス

このリポジトリのコードは [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/deed.ja) で公開しています。
著作権表示なしで、コンテストへの提出を含め、コピー・改変・再配布・商用利用を自由に行えます。詳細は [LICENSE](LICENSE) を参照してください。
