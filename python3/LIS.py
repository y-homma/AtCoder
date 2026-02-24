import sys
from bisect import bisect_left

def LIS(): #数列の最長増加列を求める
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    DP = [N + 2] * N
    for i, a in enumerate(A):
        j = bisect_left(DP, a)
        DP[j] = min(DP[j], a)
    print(bisect_left(DP, N + 1))

    return 0

if __name__ == "__main__":
    LIS()
