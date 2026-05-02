import sys
from collections import deque

def solve():
    input = sys.stdin.readline 
    X = input().strip("\n")
    L = len(X)
    N = [int(X[i]) for i in range(L)]
    S = sum(N)
    ans = 0
    O = deque()
    for i in reversed(range(L)):
        ans += S
        O.appendleft(str(ans % 10))
        S -= N[i]
        ans //= 10
    if ans > 0:
        O.appendleft(str(ans))

    print(*O, sep="")

    return 0
  
if __name__ == "__main__":
    solve()