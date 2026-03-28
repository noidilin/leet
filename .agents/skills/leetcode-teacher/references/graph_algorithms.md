# Graph Algorithms

These topics build on graph representation and traversal foundations.

## Graph DFS/BFS Review

- For: reachability and traversal review before advanced graph algorithms.
- Signals: visit all reachable nodes, connected components, path existence.
- Need first: graph representation and traversal basics.
- Model: graph traversal is tree traversal plus a `visited` set.
- Steps: pick DFS or BFS, then mark nodes early.
- Python:

```python
def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(graph, nei, visited)
```

- Interview: say this review is the base for cycle detection, topo sort, and bipartite checking.
- Mistakes: forgetting visited checks.
- Product: explore a social graph.
- Practice: components -> path existence -> traversal order.

## Cycle Detection

- For: detect whether a graph has a loop.
- Signals: dependency loop, repeated revisit on the current path.
- Need first: graph traversal.
- Model: in directed graphs, distinguish visited from currently exploring; in undirected graphs, track parent.
- Steps: choose directed or undirected rule, then traverse with the right state.
- Python:

```python
def has_cycle(graph):
    visiting, visited = set(), set()
    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for nei in graph[node]:
            if dfs(nei):
                return True
        visiting.remove(node)
        visited.add(node)
        return False
```

- Interview: clearly separate directed-graph cycle logic from undirected-graph logic.
- Mistakes: using one visited set for everything in directed graphs.
- Product: detect circular package dependencies.
- Practice: directed cycle -> course schedule variants.

## Topological Sort

- For: order tasks with prerequisite constraints.
- Signals: DAG, dependencies, valid ordering.
- Need first: cycle detection, queue or DFS.
- Model: a node can be taken only after all incoming requirements are satisfied.
- Steps: use indegree plus queue or DFS postorder.
- Python:

```python
from collections import deque

def topo_sort(graph, indegree):
    q = deque([x for x in graph if indegree[x] == 0])
    order = []
```

- Interview: explain that a full order exists only when there is no cycle.
- Mistakes: forgetting to initialize nodes with zero indegree.
- Product: build pipeline or course prerequisite order.
- Practice: topo order -> detect if all courses can finish.

## Bipartite Graph Detection

- For: check whether nodes can be split into two valid groups.
- Signals: two-coloring, dislike graph, odd-cycle property.
- Need first: graph traversal.
- Model: neighbors must always get opposite colors.
- Steps: start new traversal from each component, color as you go.
- Python:

```python
def is_bipartite(graph):
    color = {}
    for start in graph:
        if start in color:
            continue
        color[start] = 0
```

- Interview: mention the equivalence with no odd cycle.
- Mistakes: forgetting disconnected components.
- Product: split users into two conflict-free groups.
- Practice: simple two-color graph -> possible bipartition.

## Union-Find Fundamentals

- For: track connected components under repeated union operations.
- Signals: dynamic connectivity, merge groups, same-set queries.
- Need first: arrays and graph component idea.
- Model: each set has a representative parent; path compression keeps finds fast.
- Steps: `find` representative, `union` roots, optionally use rank/size.
- Python:

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
```

- Interview: explain `find` and `union` API before jumping into proofs.
- Mistakes: unioning raw nodes instead of their roots.
- Product: merging connected social groups.
- Practice: basic API -> connected components -> redundant connection.

## Union-Find Applications

- For: connectivity queries, cycle checks, component counting.
- Signals: many merge and same-group operations.
- Need first: union-find fundamentals.
- Model: every union shrinks the number of components when roots differ.
- Steps: translate problem story into `union` and `find` operations.
- Python:

```python
if uf.find(a) == uf.find(b):
    cycle = True
else:
    uf.union(a, b)
```

- Interview: say union-find is best when connectivity updates are repeated many times.
- Mistakes: using it when you actually need weighted shortest path or full traversal state.
- Product: determine whether two accounts belong to the same connected group.
- Practice: detect redundant edge -> merge accounts -> count provinces.

## MST Overview

- For: connect all nodes with minimum total edge weight.
- Signals: cheapest way to connect a network.
- Need first: weighted graphs and union-find basics.
- Model: an MST keeps all nodes connected without cycles and with minimal total cost.
- Steps: sort or prioritize edges, then keep the safe edges that do not create cycles.
- Python:

```python
# usually followed by Kruskal or Prim
```

- Interview: define spanning, tree, and minimum clearly.
- Mistakes: confusing shortest path tree with minimum spanning tree.
- Product: cheapest network cabling plan.
- Practice: identify MST goal -> compare with shortest path goal.

## Kruskal

- For: build MST by considering edges from lightest to heaviest.
- Signals: MST plus edge list representation.
- Need first: union-find and sorting.
- Model: take the lightest safe edge each time.
- Steps: sort edges, union endpoints if they are in different sets, stop after `n - 1` edges.
- Python:

```python
edges.sort(key=lambda e: e[2])
cost = 0
for u, v, w in edges:
    if uf.find(u) != uf.find(v):
        uf.union(u, v)
        cost += w
```

- Interview: say Kruskal is basically sorting plus union-find.
- Mistakes: forgetting to stop after enough edges.
- Product: connect offices with minimum cable cost.
- Practice: small MST by hand -> Kruskal coding template.

## Shortest Path Overview

- For: compare shortest path problem families.
- Signals: minimum cost from one source or between all pairs.
- Need first: graph weights and BFS basics.
- Model: unweighted shortest path uses BFS; weighted shortest path often needs Dijkstra or other algorithms.
- Steps: first ask whether edges are weighted, negative, or constrained.
- Python:

```python
# unweighted -> BFS
# weighted non-negative -> Dijkstra
```

- Interview: classify before choosing the algorithm.
- Mistakes: using plain BFS on weighted graphs.
- Product: route planning with different travel times.
- Practice: unweighted vs weighted comparison.

## Dijkstra

- For: single-source shortest path with non-negative weights.
- Signals: weighted graph, best-known distance relaxation.
- Need first: heap basics, shortest path overview.
- Model: always expand the currently cheapest unfinished state.
- Steps: store `(distance, node)` in a min-heap, relax outgoing edges, skip stale heap entries.
- Python:

```python
import heapq

def dijkstra(graph, start):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
```

- Interview: connect Dijkstra to BFS with a priority queue replacing the plain queue.
- Mistakes: forgetting stale-state check or using it on negative weights.
- Product: route planning with weighted roads.
- Practice: plain Dijkstra -> network delay style problems.

## Dijkstra With Constraints

- For: shortest path where state includes more than just node position.
- Signals: limited stops, discounts, fuel, or extra resources.
- Need first: Dijkstra.
- Model: treat `(node, extra_state)` as the real graph node.
- Steps: expand state space, store best distance per full state, then run heap-based search.
- Python:

```python
# state example: (cost, node, stops_used)
```

- Interview: say constraints often turn shortest path into shortest path on an expanded graph.
- Mistakes: tracking only node and losing constraint information.
- Product: cheapest flight with at most k stops.
- Practice: k-stop flights -> coupon discount variants.
