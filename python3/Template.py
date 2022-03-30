import sys
import collections

class Alphabet: #Trueなら大文字
    def __init__(self, capitalize):
        self.indexOf = dict() #アルファベットを数字に変換
        self.abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"\
            ,"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        if capitalize: 
            for i in range(26): self.abc[i] = self.abc[i].upper()
        for i, a in enumerate(self.abc): self.indexOf[a] = i

class Math:
    def __init__(self):
        return

    # Σ0,N-1 floor((A * i + B) / M)を求める
    def floorSum(self, n, m, a, b):
        ans = 0
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m

        y_max = (a * n + b) // m
        x_max = (y_max * m - b)
        if y_max == 0: return ans
        ans += (n - (x_max + a - 1) // a) * y_max
        ans += self.floorSum(y_max, a, m, (a - x_max % a) % a)
        return ans

    def gcd(a, b):
        a, b = max(a, b), min(a, b)
        while a % b > 0: a, b = b, a % b
        return b
  
def solve():
    file = sys.stdin.readline 
    INF = 10 ** 25
    mod = 7 + 10 ** 9
    return 0
  
if __name__ == "__main__":
    solve()
