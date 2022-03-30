import sys
from collections import deque

def topologicalSort():
    input = sys.stdin.readline
    V, E = map(int, input().split())
    Parent_node = [0 for _ in range(V)]
    Son_node = [set() for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split()) #default: 0-indexed
        Son_node[a] |= {b}
        Parent_node[b] += 1

    stack = deque() #入次数が0のノードを格納する
    for i, p in enumerate(Parent_node):
        if p == 0: stack.append(i)

    sortedArray = []
    while stack:
        nowNode = stack.popleft()
        sortedArray.append(nowNode)
        for nextNode in Son_node[nowNode]:
            Parent_node[nextNode] -= 1
            if Parent_node[nextNode] == 0: stack.append(nextNode)

    for a in sortedArray: print(a)

    return len(sortedArray) == V

if __name__ == "__main__":
    topologicalSort()