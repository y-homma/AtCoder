def inversion(A) -> int:
    """転倒数 (i < j かつ A[i] > A[j] の組の数)。O(N log N)
    A の値は任意（負・重複・大きい値も可。座標圧縮する）
    """
    idx = {v: i + 1 for i, v in enumerate(sorted(set(A)))}
    n = len(idx)
    bit = [0] * (n + 1)
    ans = 0
    for i, a in enumerate(A):
        j = idx[a]
        # これまでの要素のうち a 以下の個数
        s = 0
        k = j
        while k > 0:
            s += bit[k]
            k -= k & -k
        ans += i - s
        while j <= n:
            bit[j] += 1
            j += j & -j
    return ans
