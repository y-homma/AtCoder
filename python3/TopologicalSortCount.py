def count_topological_sort(N: int, edges, mod: int | None = None) -> int:
    """トポロジカル順序の個数を bit DP で数える。O(2^N · N)、N ≲ 20 程度
    edges: [(u, v), ...]  u -> v の有向辺（0-indexed, u を v より先に置く）
    mod を指定するとその余りを返す
    """
    pred = [0] * N  # pred[v]: v より先に置く必要がある頂点の集合
    for u, v in edges:
        pred[v] |= 1 << u
    dp = [0] * (1 << N)
    dp[0] = 1
    for S in range(1 << N):  # S: すでに並べた頂点の集合
        x = dp[S]
        if x == 0: continue
        if mod is not None: x %= mod; dp[S] = x
        for v in range(N):
            if not (S >> v) & 1 and (pred[v] & S) == pred[v]:
                dp[S | 1 << v] += x
    return dp[-1] % mod if mod is not None else dp[-1]
