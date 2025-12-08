import math
import re
import sys

lines = [line.strip() for line in sys.stdin]
arrayint = lambda arr: list(int(x) for x in arr)

# >v<^
SLOPE = list(">v<^")
DIR = ((0, 1), (1, 0), (0, -1), (-1, 0))

a = []
for line in lines:
    a.append(tuple(map(int, line.split(","))))
n = len(a)


class DSU:
    def __init__(self, n):
        # parent[i] stores the parent of element i.
        # If parent[i] == i, then i is the root of its set.
        self.parent = list(range(n))
        # size[i] stores the size of the set rooted at i.
        # Only meaningful for root nodes.
        self.size = [1] * n

    def find(self, i):
        # Path compression: make every node in the path point directly to the root.
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            # Union by size: attach the smaller tree to the root of the larger tree.
            if self.size[root_i] < self.size[root_j]:
                self.parent[root_i] = root_j
                self.size[root_j] += self.size[root_i]
            else:
                self.parent[root_j] = root_i
                self.size[root_i] += self.size[root_j]
            return True  # Sets were merged
        return False  # Already in the same set


edges = []
for i in range(n):
    for j in range(i + 1, n):
        p = a[i]
        q = a[j]
        d = sum((x - x2) * (x - x2) for x, x2 in zip(p, q)) ** 0.5
        edges.append((d, i, j))
edges.sort()
dsu = DSU(n)
for d, p, q in edges[:1000]:
    dsu.union(p, q)

b = sorted([dsu.size[i] for i in range(n) if i == dsu.find(i)], reverse=True)
print(b)
x, y, z, *a = b
print(x * y * z)
