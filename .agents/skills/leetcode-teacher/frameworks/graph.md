# Graph

- Graph algorithms are a vast topic, but essentially extend binary tree structures. Start with key terminology, common implementations, and traversal algorithm templates.
- Cycle detection, topological sort, and bipartite detection are classic graph algorithms—essentially graph traversal, not difficult to master.
- Union-Find is a practical graph algorithm—learn its principles and API. Save the UF class template in advance for quick reuse in exams.
- Minimum spanning tree is a practical graph algorithm—know its definition and use cases. Kruskal's algorithm is essentially Union-Find + sorting, relatively simple.

## Union Find Template

```python
class UF:
    # the number of connected components
    _count: int
    # store the parent of each node
    parent: List[int]

    # n is the number of nodes in the graph
    def __init__(self, n: int):
        self._count = n
        self.parent = [i for i in range(n)]

    # connect node p and node q
    def union(self, p: int, q: int):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        self.parent[rootQ] = rootP
        # merge two connected components into one
        self._count -= 1

    # determine if node p and node q are connected
    def connected(self, p: int, q: int) -> bool:
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # return the number of connected components in the graph
    def count(self) -> int:
        return self._count
```

## Leetcode Exercise

- '133. Clone Graph'
- '785. Is Graph Bipartite?''
- '886. Possible Bipartition'
- '207. Course Schedule'
- '210. Course Schedule II'
- '990. Satisfiability of Equality Equations'
- '1135. Connecting Cities With Minimum Cost'
- '1584. Min Cost to Connect All Points'
