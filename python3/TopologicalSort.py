from collections import deque


def topological_sort(N: int, edges):
    """トポロジカルソート (Kahn 法)。O(N + M)
    edges: [(u, v), ...]  u -> v の有向辺（0-indexed）
    戻り値: 頂点の並び（リスト）。閉路があれば None
    辞書順最小が欲しいときは deque の代わりに heapq を使う
    """
    g = [[] for _ in range(N)]
    indeg = [0] * N
    for u, v in edges:
        g[u].append(v)
        indeg[v] += 1

    q = deque(i for i in range(N) if indeg[i] == 0)
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for to in g[v]:
            indeg[to] -= 1
            if indeg[to] == 0: q.append(to)

    return order if len(order) == N else None
