INF = 1 << 60


def bellman_ford(N: int, edges, s: int = 0):
    """単一始点最短路（負辺 OK）。O(NM)
    edges: [(from, to, cost), ...]（0-indexed）
    戻り値: (dist, neg)
      dist[v]: s から v への最短距離。到達不能なら INF、負閉路の影響で -∞ なら -INF
      neg: s から到達できる負閉路があれば True
    """
    dist = [INF] * N
    dist[s] = 0
    for _ in range(N - 1):
        update = False
        for u, v, c in edges:
            if dist[u] != INF and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                update = True
        if not update: return dist, False

    # さらに N 回緩和して、まだ更新される頂点（とその先）を -INF にする
    neg = False
    for _ in range(N):
        for u, v, c in edges:
            if dist[u] != INF and (dist[u] == -INF or dist[v] > dist[u] + c):
                if dist[v] != -INF:
                    dist[v] = -INF
                    neg = True
    return dist, neg
