import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from math import sqrt

class Math:
    def __init__(self):
        return

    # Σ0,N-1 floor((A * i + B) / M)を求める
    def floorSum(self, n, m, a, b):
        ans = 0
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m

        y_max = (a * n + b) // m
        x_max = (y_max * m - b)
        if y_max == 0: return ans
        ans += (n - (x_max + a - 1) // a) * y_max
        ans += self.floorSum(y_max, a, m, (a - x_max % a) % a)
        return ans

    # 指定した2数のGCDを取ります
    def gcd(self, a, b):
        a, b = max(a, b), min(a, b)
        while a % b > 0: a, b = b, a % b
        return b

def inc(pi, pj, M):
    if pi[0] == pj[0]:
        return (0, 1)
    else:
        dx = pj[0] - pi[0]
        dy = pj[1] - pi[1]
        if dx < 0:
            dx *= -1
            dy *= -1
        if dy == 0:
            return (1, 0)
        d = M.gcd(dx, abs(dy))
        return (dx // d, dy // d)

def isLine(d1, d2, d3):
    if d1 == d2 or d2 == d3 or d3 == d1:
        return True
    return False
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    M = Math()
    P = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i, p in enumerate(P[:N-2]):
        for j in range(i+1, N-1):
            pj = P[j]
            dij = inc(p, pj, M)
            for k in range(j+1, N):
                pk = P[k]
                djk = inc(pj, pk, M)
                dki = inc(pk, p, M)
                if isLine(dij, djk, dki):
                    ans += 0
                else:
                    ans += 1
    print(ans)

    return 0
  
if __name__ == "__main__":
    solve()