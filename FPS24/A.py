import sys
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    mod = 998244353
    D, N = map(int, input().split())
    fact = [1] * (D + 1)
    revFact = [1] * (D + 1)
    for i in range(1, D + 1):
        fact[i] = (i * fact[i-1]) % mod
    revFact[D] = pow(fact[D], -1, mod) % mod
    for i in reversed(range(1, D)):
        revFact[i] = ((i + 1) * revFact[i+1]) % mod

    dCi = [1] * (D + 1)
    for i in range(1, D + 1):
        dCi[i] = (fact[D] * revFact[D-i] * revFact[i]) % mod

    ans = 0
    for i in range(D + 1):
        if 2 * i > N - D: break
        if (N - D - 2 * i) % 3 > 0: continue
        i3 = (N - D - 2 * i) // 3
        if i3 > D: continue
        ans += (dCi[i] * dCi[i3]) % mod
        ans %= mod
    
    print(ans)

    return 0
  
if __name__ == "__main__":
    solve()