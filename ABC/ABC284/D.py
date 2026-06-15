import sys
from math import sqrt

def solve():
    input = sys.stdin.readline 
    T = int(input())
    ans = [None] * T
    for t in range(T):
        N = int(input())
        for i in range(2, N+1):
            if N % i == 0:
                count = 0
                while N % i == 0:
                    N //= i
                    count += 1
                if count > 1:
                    ans[t] = (i, N)
                else:
                    ans[t] = (int(sqrt(N)), i)
                break
    for a in ans:
        print(*a)

    return 0 
  
if __name__ == "__main__":
    solve() 