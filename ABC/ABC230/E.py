import sys
from collections import deque, defaultdict
# from sortedcontainers import SortedSet, SortedList, SortedDict
# from itertools import permutations
# from bisect import bisect_left
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    ans = 0
    prev = N
    searched = N + 1
    for i in range(2, N):
        if (i - 1) * (i - 1) > N: break
        next = N // i
        # if i * next == N:
        #     next += 1
       #  print(f"Next {next}, i {i}, add {prev - next}, prev {prev}")
        ans += (i - 1) * (prev - next)
        
        prev = next
        searched = next + 1
    
    for i in range(1, searched):
        ans += N // i
    print(ans)
    return 0
  
if __name__ == "__main__":
    solve()