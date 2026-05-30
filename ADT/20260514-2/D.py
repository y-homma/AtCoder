import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    s = [input().strip("\n") for _ in range(3)]
    T = input().strip("\n")
    ans = [""] * len(T)
    for i in range(len(T)):
        idx = int(T[i]) - 1
        ans[i] = s[idx]
    print("".join(ans))
    
    return 0
  
if __name__ == "__main__":
    solve()