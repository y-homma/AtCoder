import sys
# from collections import deque
# from itertools import permutations
# from heapq import heapify, heappop, heappush
# from sortedcontainers import SortedSet, SortedList, SortedDict
# import bisect
sys.setrecursionlimit(10**6)

class BIT: #1-indexed
    def __init__(self, bitSize, mod):
        self.array = [0] * (bitSize + 1)
        self.size = bitSize
        self.mod = mod
    
    def sum(self, index): #[1, index]の和
        s = 0
        while index > 0:
            s += self.array[index]
            s %= self.mod
            index -= index & (-index)
        return s
 
    def add(self, index, value): #BIT[index]にvalueを加算する
        while index <= self.size:
            self.array[index] += value
            self.array[index] %= self.mod
            index += index & (-index)
        return
    
def solve():
    input = sys.stdin.readline 
    N = int(input())
    A =list(map(int, input().split()))
    mod = 998244353
    pow2 = [1] * (N + 1)
    for i in range(1, N+1):
        pow2[i] = (pow2[i-1] * 2) % mod
    revPow2 = [1] * (N + 1)
    revPow2[N] = pow(pow2[N], -1, mod)
    for i in reversed(range(1, N)):
        revPow2[i] = (revPow2[i+1] * 2) % mod
    
    AI = [(A[i], i) for i in range(N)]
    AI.sort()
    B = BIT(N, mod)
    ans = 0
    Div = [1] * (N + 1)
    for i, ai in enumerate(AI):
        aidx = ai[1]
        Div[aidx] = B.sum(aidx + 1)
        B.add(aidx + 1, revPow2[aidx+1])
    for j in range(N):
        ans += (pow2[j] * Div[j]) % mod
        ans %= mod
    print(ans)
                            
if __name__ == "__main__":
    solve() 
