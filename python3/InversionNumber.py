def inversion(N, A): #数列Aの転倒数をBITを用いて求める
    BIT = [0] * (N + 1)
    ans = 0
    for i, a in enumerate(A):
        sumA = 0
        j = a
        while j > 0:
            sumA += BIT[j]
            j -= j & -j
        ans += i - sumA
        k = a
        while k <= N:
            BIT[k] += 1
            k += k & -k
    return ans
