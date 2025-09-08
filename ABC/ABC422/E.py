import sys
from random import randint
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    mod = 7 + 10 ** 9
    N = int(input())
    P = [[0, 0] for _ in range(N)]
    for i in range(N):
        x, y = map(int, input().split())
        P[i] = [x, y]
    half = N // 2
    
    ans = "No"
    for _ in range(100):
        p1 = randint(0, N-1)
        p2 = randint(0, N-1)
        if p1 == p2: continue
        x1, y1 = P[p1]
        x2, y2 = P[p2]
        a = y2 - y1
        b = x1 - x2
        c = x2 * y1 - x1 * y2
        count = 0
        for p in P:
            if a * p[0] + b * p[1] + c == 0:
                count += 1
        if count > half:
            print("Yes")
            print("{} {} {}".format(a, b, c))
            return 0

    print(ans)
    return 0
  
if __name__ == "__main__":
    solve()