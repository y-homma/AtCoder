import sys
# from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
# sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    H, W, K = map(int, input().split())
    S = [input().strip("\n") for _ in range(H)]
    T = [[0] * (W+1) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            T[h][w+1] = T[h][w] + int(S[h][w])

    ans = 0
    for w1 in range(W):
        for w2 in range(w1, W):
            heq = 0
            teq = 0
            hov = 0
            tov = 0
            for h1 in range(H):
                while heq < H and teq < K:
                    teq += T[heq][w2+1] - T[heq][w1]
                    heq += 1
                while hov < H and tov <= K:
                    tov += T[hov][w2+1] - T[hov][w1]
                    hov += 1
                ans += (hov - heq)
                sub = T[h1][w2+1] - T[h1][w1]
                teq -= sub
                tov -= sub

    print(ans)
    
    return 0
                            
if __name__ == "__main__":
    solve() 