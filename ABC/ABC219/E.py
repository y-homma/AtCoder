import sys
from collections import deque

def isIn(h, w):
    return 0 <= h < 4 and 0 <= w < 4

def solve():
    input = sys.stdin.readline

    A = [list(map(int, input().split())) for _ in range(4)]
    D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    Edge = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 3), (2, 0), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
    ans = 0
    for i in range(1 << 16): #0: out, 1: in
        B = [[0, 0, 0, 0] for _ in range(4)]
        K = i
        inside = []
        for j in range(16):
            h = j // 4
            w = j % 4
            flg = K % 2
            B[h][w] = flg
            K >>= 1
            if flg == 1:
                inside.append((h, w))
        
        isAllIn = True
        for h in range(4):
            for w in range(4):
                if B[h][w] == 0:
                    if A[h][w] == 1:
                        isAllIn = False
                        break
            if not isAllIn:
                break
        if not isAllIn:
            continue

        connect = set()
        Q = deque()
        Q.append(inside[0])
        while len(Q) > 0:
            h, w = Q.popleft()
            idx = 4 * h + w
            if idx not in connect:
                connect.add(idx)
                for dh, dw in D:
                    nh = h + dh
                    nw = w + dw
                    nidx = 4 * nh + nw
                    if isIn(nh, nw) and B[nh][nw] == 1 and nidx not in connect:
                        Q.append((nh, nw))
        if len(connect) != len(inside):
            continue
        
        O = [[False] * 4 for _ in range(4)]
        Q.clear()
        for e in Edge:
            if B[e[0]][e[1]] == 0:
                Q.append(e)
        while len(Q) > 0:
            h, w = Q.popleft()
            if not O[h][w]:
                O[h][w] = True
                for dh, dw in D:
                    nh = h + dh
                    nw = w + dw
                    if isIn(nh, nw) and B[nh][nw] == 0 and not O[nh][nw]:
                        Q.append((nh, nw))

        isOutInner = False
        for h in range(4):
            for w in range(4):
                if B[h][w] == 0 and not O[h][w]:
                    isOutInner = True
                    break
            if isOutInner:
                break
        if isOutInner:
            continue
        ans += 1
    print(ans)

    return 0

if __name__ == "__main__":
    solve()
