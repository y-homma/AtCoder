import sys

def dfs(node, sink, f, used, Edge): #最大流量fを返す
    if node == sink: return f
    used[node] = True
    for i, e in enumerate(Edge[node]):
        nextnode, nextcap, edgeIndex = e
        if not used[nextnode] and nextcap > 0: #次の行先が未探索で容量がある場合
            d = dfs(nextnode, sink, min(f, nextcap), used, Edge) 
            if d > 0:
                Edge[node][i][1] -= d
                Edge[nextnode][edgeIndex][1] += d
                return d
    return 0

def MF(): #頂点数V、辺数Eのグラフの最大流を返す
    input = sys.stdin.readline
    V, E = map(int, input().split())
    Edge = [[] for _ in range(V)]
    edgeSize = [0] * V
    for _ in range(E): #frmからtへ容量capの辺の入力を受ける(0-index)
        frm, t, cap = map(int, input().split())
        Edge[frm].append([t, cap, edgeSize[t]])
        Edge[t].append([frm, 0, edgeSize[frm]])
        edgeSize[t] += 1
        edgeSize[frm] += 1

    maxFlow = 0
    while True:
        visited = [False for _ in range(V)]
        f = dfs(0, V - 1, 1000000000, visited, Edge)
        if f == 0: break
        maxFlow += f
    print(maxFlow)
    
    return 0

if __name__ == "__main__":
    MF()