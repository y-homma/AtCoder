import sys
from collections import deque
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    N = int(input())
    edge = [[] for _ in range(N)]
    start = -1
    for _ in range(N - 1):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        edge[v-1].append(u-1)
        start = u - 1
    color = [-1 for _ in range(N)]
    q = deque()
    q.append((start, 0))
    while len(q) > 0:
        node, c = q.popleft()
        if color[node] == -1:
            color[node] = c
            for nextNode in edge[node]:
                if color[nextNode] == -1:
                    q.append((nextNode, (c + 1) % 2))
    validEdge = set()
    for i in range(N-1):
        for j in range(i+1, N):
            if color[i] != color[j] and j not in edge[i]:
                validEdge.add(str(i + 1) + " " + str(j + 1))
    
    countA = color.count(0)
    countB = color.count(1)
    addEdge = countA * countB - (N - 1)
    if addEdge % 2 == 0:
        print("Second", flush=True)
    else:
        print("First", flush=True)
        ans = validEdge.pop()
        print(ans, flush=True)
    
    while len(validEdge) > 0:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break
        validEdge.remove(str(u) + " " + str(v))
        ans = validEdge.pop()
        print(ans, flush=True)

    return 0
  
if __name__ == "__main__":
    solve()
