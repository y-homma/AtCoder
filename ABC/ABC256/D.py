import sys
from collections import deque
  
def solve():
    input = sys.stdin.readline 
    N = int(input())
    sections = [list(map(int, input().split())) for _ in range(N)]
    sections.sort()

    ans = []
    left = sections[0][0]
    right = sections[0][1]
    for _, s in enumerate(sections[1:]):
        cl, cr = s
        if cl <= right:
            right = max(cr, right)
        else:
            ans.append((left, right))
            left = cl
            right = cr
    ans.append((left, right))
    for a in ans:
        print(*a)
 
    return 0
  
if __name__ == "__main__":
    solve()