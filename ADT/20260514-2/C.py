import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    div = []
    for i in range(1, 10):
        if N % i == 0:
            div.append(i)

    ans = ["-"] * (N + 1)
    for i in range(N+1):
        for j in div:
            k = N // j
            if i % k == 0:
                ans[i] = str(j)
                break
        else:
            ans[i] = "-"
    print("".join(ans))
    return 0
  
if __name__ == "__main__":
    solve()