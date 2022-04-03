import queue
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

    # 指定したIndexの英文字を取得します
    def get(self, index):
        return self.abc[index]

    # 指定した英文字のインデックスを取得します
    def indexOf(self, chr):
        return self.indexOf[chr]

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

    # 指定した2数のGCDを取ります
    def gcd(a, b):
        a, b = max(a, b), min(a, b)
        while a % b > 0: a, b = b, a % b
        return b

class SegTree:
    def __init__(self, N, defaultValue, isLower):
        nextP2 = 1
        while nextP2 < N:
            nextP2 *= 2
        self.tree = [defaultValue] * (nextP2 * 2 - 1)
        self.base = nextP2 - 1
        self.size = nextP2
        self.isLower = isLower
        self.defaultValue = defaultValue
 
    def update(self, value, index):
        self.tree[self.base + index] = value
        toUpdateIndex = self.base + index
        while toUpdateIndex > 0:
            toUpdateIndex = (toUpdateIndex - 1) // 2
            if self.isLower:
                self.tree[toUpdateIndex] = min(self.tree[toUpdateIndex * 2 + 1], self.tree[toUpdateIndex * 2 + 2])
            else:
                self.tree[toUpdateIndex] = max(self.tree[toUpdateIndex * 2 + 1], self.tree[toUpdateIndex * 2 + 2])
    
    def findInner(self, lowerBound, upperBound, left, right, index):
        if lowerBound <= left and right <= upperBound:
            return self.tree[index]
        if upperBound < left or right < lowerBound:
            return self.defaultValue
        half = (left + right) // 2
        leftHalf = self.findInner(lowerBound, upperBound, left, half, 2 * index + 1)
        rightHalf = self.findInner(lowerBound, upperBound, half + 1, right, 2 * index + 2)
        if self.isLower:
            return min(leftHalf, rightHalf)
        else:
            return max(leftHalf, rightHalf)
 
    def find(self, lowerBound, upperBound):
        return self.findInner(lowerBound, upperBound, 0, self.size - 1, 0)
  
def solve():
    input = sys.stdin.readline 
    INF = 10 ** 25
    mod = 7 + 10 ** 9
    N = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    S = [input() for _ in range(N)]

    if (ax + ay) % 2 != (bx + by) % 2: print(-1)
    else:
        queue = collections.deque()
        dist = [[[INF, INF, INF, INF] for _ in range(N)] for i in range(N)]
        fin = [[[False, False, False, False] for _ in range(N)] for i in range(N)]
        fin[ax - 1][ay - 1] = [True, True, True, True]
        dist[ax - 1][ay - 1] = [0, 0, 0, 0]
        direc = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in range(4):
            dx, dy = direc[i]
            nx, ny = ax - 1 + dx, ay - 1 + dy
            if nx < 0 or N <= nx or ny < 0 or N <= ny: continue
            if S[nx][ny] == "#": continue
            queue.append((1, nx, ny, i))
            dist[nx][ny][i] = 1
        
        while queue:
            d, cx, cy, flg = queue.popleft()
            if cx == bx - 1 and cy == by - 1:
                print(d)
                break
            if not fin[cx][cy][flg]:
                fin[cx][cy][flg] = True
                for i in range(4):
                    dx, dy = direc[i]
                    nx, ny = cx + dx, cy + dy
                    add = 0
                    if i != flg: add = 1
                    if nx < 0 or N <= nx or ny < 0 or N <= ny: continue
                    if S[nx][ny] == "#": continue
                    if d + add < dist[nx][ny][i]:
                        if i == flg: 
                            queue.appendleft((d, nx, ny, i))
                            dist[nx][ny][i] = d
                        else: 
                            queue.append((d + 1, nx, ny, i))
                            dist[nx][ny][i] = d + 1
        else: print(-1)

    return 0
  
if __name__ == "__main__":
    solve()
