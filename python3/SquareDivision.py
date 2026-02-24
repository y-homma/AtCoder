class SquareDiv(): #区間の最大値を求める
    def __init__(self, N, V):
        k = 1
        while k ** 2 < N: k += 1
        self.array = [V] * k
        self.size = k
        self.indivisual = [V] * N

    def update(self, i, v): #i番目をvに更新する
        self.indivisual[i] = v
        self.array[i // self.size] = max(self.array[i // self.size], v)

    def search(self, left, right): #[left, right]の最大値を求める
        lk, rk = left // self.size, right // self.size
        if lk == rk:
            maxN = 0
            for i in range(left, right + 1): maxN = max(maxN, self.indivisual[i])
            return maxN
        else:
            maxN = self.search(left, (lk + 1) * self.size - 1)
            for k in range(lk + 1, rk): maxN = max(maxN, self.array[k])
            maxN = max(maxN, self.search(rk * self.size, right))
            return maxN