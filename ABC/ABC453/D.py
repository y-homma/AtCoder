import sys
from collections import deque
    
def canMove(h, w, H, W, S):
    return 0 <= h and h < H and 0 <= w and w < W and S[h][w] != "#"
  
def solve():
    INF = 1000000000
    input = sys.stdin.readline 
    H, W = map(int, input().split())
    S = [input().strip("\n") for _ in range(H)]
    dist = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1)
    }
    DI = {
        "U": 0,
        "D": 1,
        "L": 2,
        "R": 3
    }
    
    sh, sw = 0, 0
    gh, gw = 0, 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "S":
                sh = h
                sw = w
            elif S[h][w] == "G":
                gh = h
                gw = w
    D = [[[INF, INF, INF, INF] for w in range(W)] for _ in range(H)]
    D[sh][sw] = [0, 0, 0, 0]
    Q = deque()
    for k, v in dist.items():
        nh = sh + v[0]
        nw = sw + v[1]
        if canMove(nh, nw, H, W, S):
            Q.append((1, nh, nw, k))
    
    while len(Q) > 0:
        d, ch, cw, m = Q.popleft()
        mi = DI[m]
        if d < D[ch][cw][mi]:
            D[ch][cw][mi] = d
            if ch == gh and cw == gw: break
            for k, v in dist.items():
                nh = ch + v[0]
                nw = cw + v[1]
                ki = DI[k]
                if canMove(nh, nw, H, W, S) and d + 1 < D[nh][nw][ki]:
                    if S[ch][cw] == "o" and m != k:
                        continue
                    elif S[ch][cw] == "x" and m == k:
                        continue
                    Q.append((d+1, nh, nw, k))
    
    minMove = min(D[gh][gw])
    if minMove > 5 * 10 ** 6:
        print("No")
    else:
        direction = ["U", "D", "L", "R"]
        ans = deque()
        bh = gh
        bw = gw
        ci = 0
        for i in range(4):
            if D[bh][bw][i] == minMove:
                ci = i
                break
        
        for bs in reversed(range(minMove)):
            rd = direction[ci]
            ans.appendleft(rd)
            rdist = dist[rd]
            bh -= rdist[0]
            bw -= rdist[1]
            for i in range(4):
                if D[bh][bw][i] == bs:
                    if S[bh][bw] == "o" and ci != i: 
                        continue
                    elif S[bh][bw] == "#" and ci == i:
                        continue
                    ci = i
                    # print(f"{bh}, {bw}, {bi}")
                    break
        print("Yes")
        print(*ans, sep="")
            
    return 0
  
if __name__ == "__main__":
    solve()