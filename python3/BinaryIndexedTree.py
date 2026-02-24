class BIT: #1-indexed
    def __init__(self, bitSize):
        self.array = [0] * (bitSize + 1)
        self.size = bitSize
    
    def sum(self, index): #[1, index]の和
        s = 0
        while index > 0:
            s += self.array[index]
            index -= index & (-index)
        return s
 
    def add(self, index, value): #BIT[index]にvalueを加算する
        while index <= self.size:
            self.array[index] += value
            index += index & (-index)
        return