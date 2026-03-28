# Data Structure Foundations

This file covers the structures you should understand before heavier problem-solving practice.

## Arrays Fundamentals

- For: sequential storage with fast random access.
- Signals: index-based access, contiguous memory, fixed-order traversal.
- Need first: basic variables, loops, and indexing.
- Model: an array is a row of boxes where reading by index is cheap but inserting in the middle shifts later boxes.
- Steps: identify read-heavy vs update-heavy use, then decide whether array tradeoffs fit.
- Python:

```python
arr = [1, 2, 3]
first = arr[0]
arr.append(4)
```

- Interview: say access is `O(1)`, search is usually `O(n)`, and middle insert/delete is `O(n)`.
- Mistakes: forgetting bounds, confusing value with index, assuming front insert is cheap.
- Product: an app feed rendered as an ordered list of posts.
- Practice: read/write by index -> simulate insert/delete -> trace traversal.

## Linked Lists Fundamentals

- For: pointer-based storage where local insert/delete is cheap once you already have the node.
- Signals: lots of pointer rewiring, unknown total length, head/tail operations.
- Need first: references and simple node structures.
- Model: each node stores value plus a pointer to the next node.
- Steps: draw nodes, mark `prev`, `curr`, `next`, then rewire carefully.
- Python:

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

- Interview: say access is `O(n)` but local insertion/deletion can be `O(1)`.
- Mistakes: losing `next`, forgetting dummy nodes, skipping `None` checks.
- Product: browser history pages linked one after another.
- Practice: build a list -> iterate -> insert after node -> delete next node.

## Circular Array

- For: queue-like behavior on top of array storage.
- Signals: wrap-around indexes, ring buffer, repeated head/tail movement.
- Need first: arrays and modulo arithmetic.
- Model: the physical array is fixed, but logical head and tail rotate.
- Steps: store `head`, `size`, and map logical index with modulo.
- Python:

```python
index = (head + offset) % capacity
```

- Interview: explain how it gives `O(1)` head/tail movement without shifting the whole array.
- Mistakes: forgetting modulo, mixing full and empty states, off-by-one errors.
- Product: task buffer for recent notifications.
- Practice: push/pop one end -> queue implementation -> deque simulation.

## Queue Fundamentals

- For: first-in, first-out processing.
- Signals: level order, scheduling, tasks handled in arrival order.
- Need first: arrays or linked lists.
- Model: the earliest item leaves first.
- Steps: enqueue at one end, dequeue at the other.
- Python:

```python
from collections import deque

queue = deque()
queue.append(1)
item = queue.popleft()
```

- Interview: mention `deque` for `O(1)` enqueue and dequeue.
- Mistakes: using list `pop(0)`, mixing queue with stack behavior.
- Product: ride requests waiting to be processed.
- Practice: simple queue -> level traversal -> BFS preview.

## Stack Fundamentals

- For: last-in, first-out processing.
- Signals: undo, matching pairs, expression parsing, recursion simulation.
- Need first: arrays or linked lists.
- Model: the newest item is the first item you can remove.
- Steps: push when entering work, pop when finishing work.
- Python:

```python
stack = []
stack.append('(')
top = stack.pop()
```

- Interview: explain why stacks naturally model nested structure.
- Mistakes: popping empty stack, forgetting to check the top before popping.
- Product: undo history in a code editor.
- Practice: push/pop tracing -> valid parentheses -> monotonic stack preview.

## Hash Table Principles

- For: fast average-case lookup by key.
- Signals: counting, deduplication, complement lookup, cache-like access.
- Need first: arrays and key-value thinking.
- Model: a hash function maps a key to a bucket so we can find data quickly.
- Steps: pick key -> store or update value -> use lookup to avoid rescanning.
- Python:

```python
freq = {}
for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

- Interview: mention average `O(1)` lookup and collision handling as the main idea.
- Mistakes: forgetting collisions exist, assuming order is guaranteed, using unhashable keys.
- Product: counting hashtags in a stream of posts.
- Practice: frequency map -> two sum -> grouping by key.

## Hash Table Enhancements

- For: preserving extra structure on top of hash lookup.
- Signals: need fast lookup plus stable order or random index access.
- Need first: hash table principles, arrays, linked lists.
- Model: combine a hash table with another structure to gain new abilities.
- Steps: use hash for locating data, then use the helper structure for order or position.
- Common variants: `LinkedHashMap` style design uses a linked list to preserve recency or insertion order; `ArrayHashMap` style design uses an array to support index-based random access.
- Python:

```python
# idea sketch only
key_to_node = {}
order = []
```

- Interview: mention linked-hash style for order and array-hash style for indexable storage.
- Mistakes: forgetting to update both structures together.
- Product: recent-item cache or random-pick collection.
- Practice: describe LinkedHashMap -> describe ArrayHashMap -> preview LRU.

## Binary Tree Fundamentals

- For: hierarchical data with up to two children per node.
- Signals: recursive structure, left/right child, subtree reasoning.
- Need first: nodes and recursion basics.
- Model: each node is the root of its own smaller tree.
- Steps: focus on one node, then trust the same logic on children.
- Python:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

- Interview: say trees are the main bridge into recursive thinking.
- Mistakes: treating the whole tree at once instead of one node plus subtrees.
- Product: folder structure with at most two branches in a simplified system.
- Practice: draw a tree -> identify root/leaf/subtree -> recursive traversal.

## Binary Tree Traversal

- For: visiting every node in a meaningful order.
- Signals: need all nodes, parent-before-child, child-before-parent, or level order.
- Need first: binary tree fundamentals, queue, recursion.
- Model: preorder, inorder, postorder are three moments around the same node; level order is BFS by layers.
- Steps: decide which visit moment matches the question.
- Python:

```python
def preorder(root):
    if not root:
        return
    visit(root)
    preorder(root.left)
    preorder(root.right)
```

- Interview: explain that traversal order changes what information is available when you process a node.
- Mistakes: memorizing order names without understanding the processing moment.
- Product: rendering a menu tree or exporting nested settings.
- Practice: preorder -> inorder -> postorder -> level order.

## N-ary Tree Traversal

- For: tree structures where each node can have many children.
- Signals: folders, comments, menus, trie-like child lists.
- Need first: binary tree traversal.
- Model: the recursion idea is the same; only the child loop changes.
- Steps: process current node, then iterate through children.
- Python:

```python
def dfs(node):
    if not node:
        return
    visit(node)
    for child in node.children:
        dfs(child)
```

- Interview: say N-ary tree traversal is a direct extension of binary tree traversal.
- Mistakes: thinking N-ary traversal is a different category instead of the same idea with a loop.
- Product: comment threads with many replies.
- Practice: recursive DFS -> level order with queue -> trie preview.

## DFS Vs BFS Use Cases

- For: choosing depth-first or breadth-first traversal.
- Signals: path exploration vs shortest-layer exploration.
- Need first: stack, queue, tree traversal.
- Model: DFS goes deep first, BFS expands one layer at a time.
- Steps: ask whether you care more about full exploration or shortest unweighted steps.
- Python:

```python
# DFS often uses recursion or a stack.
# BFS often uses a queue.
```

- Interview: say BFS is the prototype for shortest path in an unweighted graph, while DFS is a natural recursive exploration tool.
- Mistakes: using DFS when the problem asks for minimum number of steps.
- Product: DFS for exploring all settings branches, BFS for minimum-click navigation.
- Practice: same graph with DFS and BFS -> compare visit order and use case.

## BST Introduction

- For: ordered tree lookup and range-style reasoning.
- Signals: left smaller, right larger, ordered traversal.
- Need first: binary trees and inorder traversal.
- Model: BST order lets you skip half of a subtree when the value cannot be there.
- Steps: compare current value with target, then move left or right.
- Python:

```python
def search_bst(root, target):
    while root and root.val != target:
        root = root.left if target < root.val else root.right
    return root
```

- Interview: mention ordered property and inorder traversal producing sorted order.
- Mistakes: forgetting worst-case can still be `O(n)` if unbalanced.
- Product: maintaining ranked IDs in a tree-like index.
- Practice: search -> insert -> delete idea preview.

## Binary Heap Principles

- For: priority queues with fast access to the smallest or largest element.
- Signals: repeatedly take best item, top-k, scheduling by priority.
- Need first: complete binary tree idea, arrays.
- Model: heap order is weaker than full sorting but strong enough for priority operations.
- Steps: push item, maintain heap property, pop best item when needed.
- Python:

```python
import heapq

heap = []
heapq.heappush(heap, 5)
best = heapq.heappop(heap)
```

- Interview: say Python uses a min-heap and each push/pop is `O(log n)`.
- Mistakes: confusing heap with fully sorted array.
- Product: always assign the closest available driver next.
- Practice: min-heap basics -> top-k -> Dijkstra preview.

## Graph Terminology And Representation

- For: modeling networks, dependencies, and relationships.
- Signals: nodes plus edges, neighbor questions, cycles, paths.
- Need first: arrays, hash tables, traversal basics.
- Model: a graph generalizes trees by allowing arbitrary connections.
- Steps: choose adjacency list first unless a dense adjacency matrix is clearly better.
- Python:

```python
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': [],
}
```

- Interview: define vertex, edge, directed, undirected, weighted, cycle, and connected component.
- Mistakes: forgetting direction, mixing node values with node indexes.
- Product: social connections or course prerequisites.
- Practice: build adjacency list -> read neighbors -> draw a small graph.

## Graph Traversal Fundamentals

- For: visiting reachable nodes in a graph.
- Signals: connected components, path existence, reachability.
- Need first: graph representation, DFS, BFS.
- Model: graph traversal is tree traversal plus a `visited` set to prevent repeats.
- Steps: choose DFS or BFS, then mark nodes when you add or enter them.
- Python:

```python
from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = {start}
    while queue:
        node = queue.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)
```

- Interview: emphasize the `visited` set as the key difference from tree traversal.
- Mistakes: marking too late, which can create duplicates or infinite loops.
- Product: degrees of connection in a social network.
- Practice: DFS traversal -> BFS traversal -> connected components preview.
