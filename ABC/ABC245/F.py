from calendar import c
from heapq import heapify, heappop
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
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    reverseEdge = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edge[u-1].append(v-1)
        reverseEdge[v-1].append(u-1)
    
    indexes = [N + 1] * N
    visited = [False] * N
    queue = [int(i) for i in reversed(range(N))]
    index = 0
    while queue:
        currentNode = queue.pop()
        if indexes[currentNode] == N + 1:
            visited[currentNode] = True
            nextNodes = []
            for nextNode in edge[currentNode]:
                if not visited[nextNode]:
                    nextNodes.append(nextNode)
            if len(nextNodes) == 0:
                indexes[currentNode] = index
                index += 1
            else:
                queue.append(currentNode)
                for nextNode in nextNodes: queue.append(nextNode)
    
    searched = [False] * N
    hq = [(-indexes[i], i) for i in range(N)]
    hq.sort()
    groups = []
    for n in hq:
        index, startNode = n
        if not searched[startNode]:
            queue2 = [startNode]
            group = []
            while queue2:
                currentNode = queue2.pop()
                if not searched[currentNode]:
                    searched[currentNode] = True
                    group.append(currentNode)
                    for nextNode in reverseEdge[currentNode]:
                        if not searched[nextNode]:
                            queue2.append(nextNode)
            groups.append(group)

    k = len(groups)
    idx = [None] * N
    for i in range(k):
        for v in groups[i]:
            idx[v] = i
    DP = [False] * k
    ans = 0
    for i in reversed(range(k)):
        if len(groups[i]) == 1:
            for v in edge[groups[i][0]]:
                DP[i] |= DP[idx[v]]
        else:
            DP[i] = True
        if DP[i]: ans += len(groups[i])
    
    print(ans)
    return 0
  
if __name__ == "__main__":
    solve()
