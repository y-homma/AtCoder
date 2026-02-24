class Node:
    def __init__(self, key, value, height):
        self.key = key #ノードの木
        self.height = height #このノードを根とする部分木の高さ
        self.value = value #ノードの値
        self.left = None
        self.right = None

    def size(self, n): return 0 if n is None else n.height

    def bias(self): #左の方が高いと正、右が高いと負の値を返す
        return self.size(self.left) - self.size(self.right)

    #木の高さの計算
    def calcSize(self):
        self.height = 1 + max(self.size(self.left), self.size(self.right))

class AVLTree:
    def __init__(self):
        self.root = None #根
        self.change = False #修正フラグ
        self.lmax = None #左部分木のキーの最大値
        self.value = None #lmaxの値

    ###############
    #回転操作, 修正操作
    ###############
    def rotateL(self, n): #ノードnの左回転
        r = n.right; rl = r.left
        r.left = n; n.right = rl
        r.left.calcSize()
        r.calcSize()
        return r

    def rotateR(self, n):
        l = n.left; lr = l.right
        l.right = n; n.left = lr
        l.right.calcSize()
        l.calcSize()
        return l

    def rotateLR(self, n): #二重回転;左回転→右回転
        n.left = self.rotateL(n.left)
        return self.rotateR(n)

    def rotateRL(self, n):
        n.right = self.rotateR(n.right)
        return self.rotateL(n)
        
    def balanceL(self, n):
        if not self.change: return n
        h = n.height
        if n.bias() == 2:
            if n.left.bias() >= 0: n = self.rotateR(n)
            else: n = self.rotateLR(n)
        else: n.calcSize()
        self.change = (h != n.height)
        return n

    def balanceR(self, n):
        if not self.change: return n
        h = n.height
        if n.bias() == -2:
            if n.right.bias() <= 0: n = self.rotateL(n)
            else: n = self.rotateRL(n)
        else: n.calcSize()
        self.change = (h != n.height)
        return n

    ###############
    #Nodeの追加
    ###############
    def insert(self, key, value): self.root = self.insert_sub(self.root, key, value)
    
    def insert_sub(self, t, key, value): #新たなノードの挿入。初期位置は根。
        if t is None:
            self.change = True
            return Node(key, value, 1)
        if key < t.key:
            t.left = self.insert_sub(t.left, key, value)
            return self.balanceL(t)
        elif key > t.key:
            t.right = self.insert_sub(t.right, key, value)
            return self.balanceR(t)
        else:
            self.change = False
            t.value = value
            return t

    ###############
    #Nodeの削除
    ###############
    def delete(self, key): self.root = self.delete_sub(self.root, key)

    def delete_sub(self, t, key):
        if t is None:
            self.change = False
            return None
        if key < t.key:
            t.left = self.delete_sub(t.left, key)
            return self.balanceR(t)
        elif key > t.key:
            t.right = self.delete_sub(t.right, key)
            return self.balanceL(t)
        else:
            if t.left is None:
                self.change = True
                return t.right
            else:
                t.left = self.delete_max(t.left)
                t.key = self.lmax
                t.value = self.value
                return self.balanceR(t)
    
    def delete_max(self, n):
        if n.right is None: #nの右部分木が存在しない場合は左部分木を昇格させる
            self.change = True
            self.lmax = n.key
            self.value = n.value
            return n.left
        else:
            n.right = self.delete_max(n.right)
            return self.balanceL(n)

    ###############
    #Nodeの探索
    ###############
    def search(self, key):
        t = self.root
        while t:
            if key < t.key: t = t.left
            elif key > t.key: t = t.right
            else: return True
        return False

    def getValue(self, key):
        t = self.root
        while t:
            if key < t.key: t = t.left
            elif key > t.key: t = t.right
            else: return t.value
        return None

    def lower_bound(self, key, leastValue):
        t = self.root
        bound = leastValue
        while t:
            if key <= t.key: t = t.left
            else:
                bound = t.key
                t = t.right
        return bound 

    def upper_bound(self, key, largestValue):
        t = self.root
        bound = largestValue
        while t:
            if key < t.key:
                bound = t.key
                t = t.left
            else: t = t.right
        return bound
                

def solve(): 
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    revP = {p: i for i, p in enumerate(P)}
    T = AVLTree()
    left = N
    right = -1
    ans = N
    for i in range(K):
        pi = revP[i+1]
        T.insert(pi, i+1)
        left = min(left, pi)
        right = max(right, pi)
    ans = min(right - left, ans)
    
    for i in range(K+1, N+1):
        remove = i - K
        ri = revP[remove]
        # print(f"remove: {remove}, index: {ri}")
        T.delete(ri)
        if ri == left:
            left = T.upper_bound(ri, ri)
        elif ri == right:
            right = T.lower_bound(ri, ri)
        pi = revP[i]
        T.insert(pi, i)
        left = min(left, pi)
        right = max(right, pi)
        ans = min(right - left, ans)
    
    print(ans)
        
    return 0

if __name__ == "__main__":
    solve()
