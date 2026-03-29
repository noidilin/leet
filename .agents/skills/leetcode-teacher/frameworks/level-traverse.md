# Level Traverse

There are three ways to write the level-order traversal of a binary tree, which can be chosen according to the actual situation. The level-order traversal of a binary tree will give rise to BFS search algorithms and shortest path algorithms.

## Level Order Simple Template

```python
from collections import deque

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    while q:
        cur = q.popleft()
        # visit cur node
        print(cur.val)

        # add cur's left and right children to the queue
        if cur.left is not None:
            q.append(cur.left)
        if cur.right is not None:
            q.append(cur.right)
```

## Level Order with Depth Template

```python
from collections import deque

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    # record the current depth being traversed (root node is considered as level 1)
    depth = 1

    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.popleft()
            # visit cur node and know its depth
            print(f"depth = {depth}, val = {cur.val}")

            # add cur's left and right children to the queue
            if cur.left is not None:
                q.append(cur.left)
            if cur.right is not None:
                q.append(cur.right)
        depth += 1
```

## Level Order Custom State

```python
class State:
    def __init__(self, node, depth):
        self.node = node
        self.depth = depth

def levelOrderTraverse(root):
    if root is None:
        return
    q = deque()
    # the path weight sum of the root node is 1
    q.append(State(root, 1))

    while q:
        cur = q.popleft()
        # visit the cur node, and know its path weight sum
        print(f"depth = {cur.depth}, val = {cur.node.val}")

        # add the left and right child nodes of cur to the queue
        if cur.node.left is not None:
            q.append(State(cur.node.left, cur.depth + 1))
        if cur.node.right is not None:
            q.append(State(cur.node.right, cur.depth + 1))
```

## Leetcode Exercise

- '102. Binary Tree Level Order Traversal'
- '117. Populating Next Right Pointers in Each Node II'
- '662. Maximum Width of Binary Tree'
- '958. Check Completeness of a Binary Tree'
