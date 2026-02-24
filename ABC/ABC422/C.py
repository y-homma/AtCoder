import sys
import collections
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    mod = 7 + 10 ** 9
    T = int(input())
    ans = [0 for _ in range(T)]
    for i in range(T):
        a, b, c = map(int, input().split())
        low, high = 0, min(a, c) + 1
        while high - low > 1:
            mid = (low + high) // 2
            # print("low: {}, high: {}".format(low, high))
            if a < mid or c < mid:
                high = mid
                continue
            lem = a + b + c - 2 * mid
            if lem < mid:
                high = mid
            elif lem:
                low = mid
        ans[i] = low

    print(*ans, sep="\n")
    return 0
  
if __name__ == "__main__":
    solve()