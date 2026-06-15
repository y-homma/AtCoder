import sys
from collections import deque
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    D = [[abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]) for j in range(N)] for i in range(N)]

    low = 0
    high = 10 ** 20
    while high - low > 1:
        mid = (low + high) // 2
        # 判定
        canMove = False
        E = [[] for _ in range(N)]
        for i in range(N):
            power = P[i][2] * mid
            for j in range(N):
                if i == j: continue
                if power >= D[i][j]:
                    E[i].append(j)
        for i in range(N):
            q = deque()
            visited = set()
            q.append(i)
            while len(q) > 0:
                ci = q.popleft()
                if ci not in visited:
                    visited.add(ci)
                    for ni in E[ci]:
                        if ni not in visited: q.append(ni)
            if len(visited) == N:
                canMove = True
                break
        else:
            canMove = False

        if canMove:
            high = mid
        else:
            low = mid
    
    print(high)
 
    return 0
  
if __name__ == "__main__":
    solve()