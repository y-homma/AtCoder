import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    SA = [0] * (N + 1)
    for i, a in enumerate(A):
        SA[i+1] = SA[i] + a
    
    y = 0
    z = 0
    w = 0
    for i in range(N):
        if y < i: y = i + 1
        while y < N and SA[y] - SA[i] < P:
            y += 1
        if SA[y] - SA[i] == P:
            if z < y: z = y + 1
            while z < N and SA[z] - SA[y] < Q:
                z += 1
            if z > N: break
            if SA[z] - SA[y] == Q:
                if w < z: w = z + 1
                while w < N and SA[w] -  SA[z] < R:
                    w += 1
                if w > N: break
                if SA[w] - SA[z] == R:
                    print("Yes")
                    return 0
    print("No")

    return 0
  
if __name__ == "__main__":
    solve()