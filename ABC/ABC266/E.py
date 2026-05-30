import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    E = [0] * (N + 1)
    for i in range(1, N+1):
        E[i] = (max(1, E[i-1]) + max(2, E[i-1]) + max(3, E[i-1]) + max(4, E[i-1]) + max(5, E[i-1]) + max(6, E[i-1])) / 6
    print(E[N])
    return 0
  
if __name__ == "__main__":
    solve()