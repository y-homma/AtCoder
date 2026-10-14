from bisect import bisect_left, bisect_right


def LIS(A, strict: bool = True) -> int:
    """最長増加部分列の長さ。O(N log N)
    strict=True: 狭義単調増加、False: 広義単調増加（非減少）
    A の値は任意（負・大きい値も可）
    """
    bs = bisect_left if strict else bisect_right
    dp = []  # dp[k]: 長さ k+1 の増加列の末尾の最小値
    for a in A:
        k = bs(dp, a)
        if k == len(dp): dp.append(a)
        else: dp[k] = a
    return len(dp)
