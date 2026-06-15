import sys
# from collections import deque
# from itertools import permutations
from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict

  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    P = [None for _ in range(N)]
    for i in range(N):
        t, d = map(int, input().split())
        P[i] = (t, t+d)
    P.sort()
    pq = []
    heapify(pq)

    current = 0
    ans = 0
    idx = 0
    while True:
        if (len(pq) == 0):
            if idx == N: break
            current = P[idx][0]

        while idx < N and P[idx][0] == current:
            heappush(pq, P[idx][1])
            idx += 1

        while len(pq) > 0:
            top = heappop(pq)
            if top >= current:
                heappush(pq, top)
                break
        
        if len(pq) > 0:
            top = heappop(pq)
            ans += 1
            current += 1

    print(ans)

    return 0
  
if __name__ == "__main__":
    solve() 