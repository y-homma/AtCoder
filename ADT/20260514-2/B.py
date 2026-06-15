import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    for i, a in enumerate(A):
        if a < X:
            X = a
            print(1)
        else:
            print(0)
    
    return 0
  
if __name__ == "__main__":
    solve()