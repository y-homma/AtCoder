import sys
from collections import deque
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(N)]
    E = [[] for _ in range(N)]
    for i in range(N-1):
        xi, yi, ri = C[i]
        for j in range(i+1, N):
            xj, yj, rj = C[j]
            if (ri - rj) ** 2 <= (xi - xj) ** 2 + (yi - yj) ** 2 <= (ri + rj) ** 2:
                E[i].append(j)
                E[j].append(i)
    Q = deque()
    for i, c in enumerate(C):
        x, y, r = c
        if (sx - x) ** 2 + (sy - y) ** 2 == r**2:
            Q.append(i)
    visited = [False] * N
    while len(Q) > 0:
        ci = Q.popleft()
        if not visited[ci]:
            visited[ci] = True
            for ni in E[ci]:
                if not visited[ni]:
                    Q.append(ni)

    for i, c in enumerate(C):
        x, y, r = c
        if (tx - x) ** 2 + (ty - y) ** 2 == r**2 and visited[i]:
            print("Yes")
            break
    else:
        print("No")
 
    return 0
  
if __name__ == "__main__":
    solve()