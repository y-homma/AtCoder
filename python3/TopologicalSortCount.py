import sys

def TSCount(): #頂点数32以下の時トポロジカルソートのとり得る並べ方を数え上げる
    N, M = map(int, input().split())
    Son = [0] * N
    nbit = [1 << i for i in range(N)] #i番目の頂点はi-bit目が1でその他は0
    for _ in range(M):
        x, y = map(int, input().split())
        Son[x - 1] |= nbit[y - 1] #頂点xから向かう頂点集合のy-bit目のbitを立てる
    DP = [0] * (1 << N)
    DP[0] = 1

    for i in range(2 ** N):
        for j, n in enumerate(nbit):
            if (i & n) == 0 and (i & Son[j]) == 0: #頂点集合iがjを含まず、jから向かう頂点集合(Son[j])も含まない時
                DP[i | n] += DP[i] #頂点集合iにjを加えた集合に加算する
    print(DP[-1])

    return 0

if __name__ == "__main__":
    TSCount()