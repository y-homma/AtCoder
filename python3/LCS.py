import sys

def LCS(s, t): #文字列sと文字列tの最長共通部分列を求める
    DP = [[0 for j in range(len(t) + 1)] for _ in range(len(s) + 1)]
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i] == t[j]: DP[i + 1][j + 1] = DP[i][j] + 1
            else: DP[i + 1][j + 1] = max(DP[i][j + 1], DP[i + 1][j])
    return DP[N][M] 


def solve():
    s = input()
    t = input()
    print(LCS(s, t))

    return 0

if __name__ == "__main__":
    solve()