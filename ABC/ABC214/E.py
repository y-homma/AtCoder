import sys
# from collections import deque
# from itertools import permutations
from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
import bisect
sys.setrecursionlimit(10**6)

def solve():
    input = sys.stdin.readline 
    T = int(input())
    Ans = ["No"] * T
    for t in range(T):
        N = int(input())
        Q = []
        heapify(Q)
        Left = set()
        BD = dict()
        for _ in range(N):
            l, r = map(int, input().split())
            Left.add(l)
            if l not in BD: BD[l] = []
            BD[l].append(r)
        Left = list(Left)
        Left.sort()
        idx = 1
        while idx <= 10 ** 9:
            if idx in BD:
                for r in BD[idx]:
                    heappush(Q, r)
            if len(Q) == 0:
                ni = bisect.bisect_left(Left, idx+1)
                if ni >= len(Left):
                    idx = 10 ** 9 + 1
                else:
                    idx = Left[ni]
            else:
                minR = heappop(Q)
                if minR < idx:
                    Ans[t] = "No"
                    break
                idx += 1
        else:
            if len(Q) > 0:
                Ans[t] = "No"
            else:
                Ans[t] = "Yes"

    print(*Ans, sep="\n")

                
    return 0
                            
if __name__ == "__main__":
    solve() 