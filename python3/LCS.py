def LCS(s, t) -> str:
    """s と t の最長共通部分列を 1 つ返す（長さだけなら len(LCS(s, t))）。O(|s||t|)
    s が文字列なら文字列、リストならリストで返す
    """
    return "".join(map(str, lcs_list(s, t))) if isinstance(s, str) else lcs_list(s, t)


def lcs_list(s, t) -> list:
    n, m = len(s), len(t)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        si = s[i]; cur = dp[i]; nxt = dp[i + 1]
        for j in range(m):
            if si == t[j]: nxt[j + 1] = cur[j] + 1
            else: nxt[j + 1] = max(cur[j + 1], nxt[j])
    # 復元
    res = []
    i, j = n, m
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            res.append(s[i - 1]); i -= 1; j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]: i -= 1
        else: j -= 1
    return res[::-1]
