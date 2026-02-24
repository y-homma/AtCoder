import sys

def solve():
    input = sys.stdin.readline 
    mod = 998244353
    maxA = 10000000
    T = int(input())
    Ans = [[] for _ in range(T)]
    minPrime = [i for i in range(maxA + 1)]
    for i in range(2, maxA + 1):
        if i == minPrime[i]:
            ci = 2 * i
            while ci <= maxA:
                minPrime[ci] = min(minPrime[ci], i)
                ci += i

    for t in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        F = [[] for i in range(N)] # (因数, n)
        G = dict() #{因数: [(最大数, 要素数), (2番目, 要素数)]}
        
        for i, a in enumerate(A):
            # 因数分解
            c = a
            while True:
                if c <= 1: break
                j = minPrime[c]
                count = 0
                while c % j == 0:
                    c //= j
                    count += 1
                F[i].append((j, count))
                if j not in G.keys():
                    G[j] = [None, None]
                if G[j][0] is None:
                    G[j][0] = [count, 1]
                else:
                    top, second = G[j]
                    if top[0] == count:
                        G[j][0][1] += 1
                    elif top[0] < count:
                        G[j][0] = [count, 1]
                        G[j][1] = top
                    else:
                        if second is None:
                            G[j][1] = [count, 1]
                        elif second[0] == count:
                            G[j][1][1] += 1
                        elif second[0] < count:
                            G[j][1] = [count, 1]
                if c == 1: break

        ans = [0] * N
        lcm = 1
        for f, l in G.items():
            p = l[0][0]
            lcm = (lcm * pow(f, p, mod)) % mod
        for i in range(N):
            tmp = lcm
            for factors in F[i]:
                f, p = factors
                g = G[f]
                if g[0][0] == p:
                    if g[0][1] == 1:
                        second = g[1]
                        if second is None:
                            tmp = (tmp * pow(f, -p, mod)) % mod
                        else:
                            tmp = (tmp * pow(f, second[0]-p, mod)) % mod
            ans[i] = tmp
        Ans[t] = ans
    for ans in Ans:
        print(*ans)

    return 0
  
if __name__ == "__main__":
    solve()