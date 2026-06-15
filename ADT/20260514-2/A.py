import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    S = input().strip("\n")
    print("Yes" if len(S) % 5 == 0 else "No")
    
    return 0
  
if __name__ == "__main__":
    solve()