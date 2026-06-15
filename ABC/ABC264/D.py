import sys
from collections import deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
  
def solve():
    input = sys.stdin.readline 
    S = input().strip("\n")
    T = "atcoder"
    count = 0
    for i in range(7):
        if S[i] == T[i]:
            continue
        else:
            si = S.find(T[i])
            count += si - i
            back = ""
            for j in range(i, 7):
                if si != j: back += S[j]
            S = S[:i] + T[i] + back
    print(count)

    return 0
  
if __name__ == "__main__":
    solve()