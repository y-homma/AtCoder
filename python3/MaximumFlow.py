from collections import deque


class MaxFlow:
    """最大流 (Dinic 法, 0-indexed)。O(V^2 E) だが実用上かなり速い
    使い方: mf = MaxFlow(N); mf.add_edge(u, v, cap); mf.flow(s, t)
    """

    def __init__(self, n: int):
        self.n = n
        self.g = [[] for _ in range(n)]  # g[v] = [[to, cap, rev], ...]
        self.pos = []                    # 辺番号 -> (from, g[from] 内の位置)

    def add_edge(self, u: int, v: int, cap: int) -> int:
        """u -> v に容量 cap の辺を追加し、辺番号を返す"""
        self.pos.append((u, len(self.g[u])))
        ru = len(self.g[u]); rv = len(self.g[v])
        if u == v: rv += 1
        self.g[u].append([v, cap, rv])
        self.g[v].append([u, 0, ru])
        return len(self.pos) - 1

    def get_edge(self, i: int):
        """辺 i の (from, to, cap, flow)"""
        u, k = self.pos[i]
        v, c, r = self.g[u][k]
        f = self.g[v][r][1]
        return u, v, c + f, f

    def flow(self, s: int, t: int, limit: int = 1 << 60) -> int:
        """s から t へ最大 limit 流し、流した量を返す"""
        assert s != t
        n, g = self.n, self.g
        total = 0
        while total < limit:
            # BFS で距離ラベル
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                for to, cap, _ in g[v]:
                    if cap > 0 and level[to] < 0:
                        level[to] = level[v] + 1
                        q.append(to)
            if level[t] < 0: break
            it = [0] * n
            # 非再帰 DFS で増加路を探す
            while total < limit:
                stack = [s]   # 頂点の列
                while stack:
                    v = stack[-1]
                    if v == t: break
                    gv = g[v]
                    while it[v] < len(gv):
                        to, cap, _ = gv[it[v]]
                        if cap > 0 and level[v] < level[to]: break
                        it[v] += 1
                    if it[v] == len(gv):
                        stack.pop()
                        level[v] = -1  # 行き止まり
                        if stack: it[stack[-1]] += 1
                    else:
                        stack.append(gv[it[v]][0])
                if not stack: break
                # 経路上の最小容量を流す
                f = limit - total
                for v in stack[:-1]:
                    f = min(f, g[v][it[v]][1])
                for v in stack[:-1]:
                    e = g[v][it[v]]
                    e[1] -= f
                    g[e[0]][e[2]][1] += f
                total += f
        return total

    def min_cut(self, s: int):
        """flow 後に呼ぶ。s 側に属する頂点なら True のリスト"""
        visited = [False] * self.n
        visited[s] = True
        stack = [s]
        while stack:
            v = stack.pop()
            for to, cap, _ in self.g[v]:
                if cap > 0 and not visited[to]:
                    visited[to] = True
                    stack.append(to)
        return visited
