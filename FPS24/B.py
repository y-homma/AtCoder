import sys
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    mod = 998244353
    N = int(input().strip("\n"))
    
    print((N + 1) % mod)

    return 0
  
if __name__ == "__main__":
    solve()