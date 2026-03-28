# Tree And Recursion Frameworks

This file treats binary tree traversal as the main bridge into recursion, DFS, backtracking, and later DP frameworks.

## Recursion From Binary Tree Perspective

- For: building recursive intuition from a concrete structure.
- Signals: a problem repeats the same rule on smaller parts.
- Need first: binary tree fundamentals and traversal.
- Model: each recursive call handles one node, and children are smaller copies of the same task.
- Steps: define what one call means, define base case, recurse on children.
- Python:

```python
def dfs(root):
    if not root:
        return
    dfs(root.left)
    dfs(root.right)
```

- Interview: say recursion becomes less mysterious when you see it as tree traversal.
- Mistakes: trying to track the whole tree at once.
- Product: recursively processing nested folders.
- Practice: simple traversal -> compute height -> count nodes.

## Traversal Thinking Vs Decompose-The-Problem Thinking

- For: choosing the right recursive viewpoint.
- Signals: either you need to update global/path state while walking, or you need each subtree to return an answer.
- Need first: recursion from binary tree perspective.
- Model: traversal thinking asks "what should I do at this node?"; decomposition asks "what should each subtree return to me?"
- Steps: decide whether information flows top-down, bottom-up, or both.
- Python:

```python
# traversal style
def traverse(root):
    if not root:
        return
    update_path(root)
    traverse(root.left)
    traverse(root.right)

# decomposition style
def solve(root):
    if not root:
        return base
    left = solve(root.left)
    right = solve(root.right)
    return combine(left, right, root)
```

- Interview: explain why the question's required output suggests one style.
- Mistakes: forcing all recursive problems into one style.
- Product: traversal for collecting logs, decomposition for computing aggregate stats.
- Practice: path sum with traversal -> max depth with decomposition.

## Preorder, Inorder, And Postorder Positions

- For: deciding when a node should be processed.
- Signals: build before children, between children, or after children.
- Need first: traversal basics.
- Model: each node has three useful moments: before left, between left and right, after right.
- Steps: map the problem's needed information to one of those moments.
- Python:

```python
def traverse(root):
    if not root:
        return
    preorder(root)
    traverse(root.left)
    inorder(root)
    traverse(root.right)
    postorder(root)
```

- Interview: say inorder matters for BST sorted order; postorder is natural when children must be solved first.
- Mistakes: memorizing names without connecting them to timing.
- Product: preorder for cloning structure, postorder for deleting structure.
- Practice: traversal order matching exercises.

## Binary Tree Construction

- For: rebuild a tree from traversal information or recursive slices.
- Signals: arrays of preorder/inorder or similar recursive structure data.
- Need first: traversal positions and recursion.
- Model: one traversal tells you the root; the other tells you subtree boundaries.
- Steps: pick root, split left/right parts, recurse.
- Python:

```python
def build(preorder, inorder_map, pre_l, pre_r, in_l, in_r):
    if pre_l > pre_r:
        return None
    root_val = preorder[pre_l]
    root = TreeNode(root_val)
    mid = inorder_map[root_val]
    left_size = mid - in_l
```

- Interview: explain how traversal order reveals root and subtree size.
- Mistakes: slicing arrays repeatedly instead of tracking indexes.
- Product: rebuilding a category tree from export data.
- Practice: build from preorder+inorder -> other reconstruction variants.

## Binary Tree Serialization

- For: converting a tree to a storable string and back.
- Signals: save/load tree structure.
- Need first: traversal and null-marker handling.
- Model: traversal order plus null markers uniquely records structure.
- Steps: pick a traversal, write null markers, then parse in the same order.
- Python:

```python
def serialize(root):
    vals = []
    def dfs(node):
        if not node:
            vals.append('#')
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
```

- Interview: state that values alone are not enough; null positions matter.
- Mistakes: forgetting null markers.
- Product: saving a tree-based document outline.
- Practice: serialize -> deserialize -> compare trees.

## Level-Order Framework

- For: layer-by-layer tree processing.
- Signals: nearest, minimum depth, level grouping.
- Need first: queue fundamentals and tree traversal.
- Model: level order is BFS on a tree.
- Steps: push root, process one queue length as one layer.
- Python:

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    queue = deque([root])
```

- Interview: connect level order in trees to BFS in graphs.
- Mistakes: mixing nodes from different levels.
- Product: render a menu one depth at a time.
- Practice: level values -> minimum depth -> right side view.

## Lowest Common Ancestor

- For: find the lowest shared ancestor of two nodes.
- Signals: two targets inside one tree.
- Need first: recursion and postorder reasoning.
- Model: each subtree reports whether it found `p`, `q`, or the answer.
- Steps: recurse left and right, then decide at current node.
- Python:

```python
def lca(root, p, q):
    if not root or root == p or root == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left or right
```

- Interview: say postorder is natural because children must report upward first.
- Mistakes: using value equality when node identity matters.
- Product: closest shared folder for two files.
- Practice: generic binary tree LCA -> BST LCA comparison.

## Complete Binary Tree Node Counting

- For: count nodes faster than plain traversal in a complete tree.
- Signals: complete binary tree property is explicitly given.
- Need first: tree height and binary tree structure.
- Model: if left and right heights match, one subtree is perfect and can be counted directly.
- Steps: compare edge heights, count one perfect side in `O(1)` formula, recurse on the other side.
- Python:

```python
def left_height(node):
    h = 0
    while node:
        h += 1
        node = node.left
    return h
```

- Interview: explain how completeness gives extra structure beyond a normal tree.
- Mistakes: applying this trick to arbitrary trees.
- Product: counting seats in a nearly full tournament bracket.
- Practice: full traversal count -> complete tree optimization.

## BST Properties And Operations

- For: search, insert, delete, kth-smallest, range checks.
- Signals: ordered tree property is useful.
- Need first: BST introduction and inorder traversal.
- Model: inorder traversal of a BST is sorted.
- Steps: compare target with current node and use left/right property to skip work.
- Python:

```python
def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    return root
```

- Interview: mention how the property prunes search space.
- Mistakes: forgetting delete has several cases.
- Product: ordered ranking tree.
- Practice: search -> validate BST -> kth smallest -> delete.

## BST Construction

- For: build a BST from insertion order or sorted data.
- Signals: BST output is required, often balanced from sorted input.
- Need first: BST properties.
- Model: sorted input naturally suggests middle element as root for a balanced tree.
- Steps: choose root, recursively build left and right ranges.
- Python:

```python
def sorted_array_to_bst(nums):
    def build(l, r):
        if l > r:
            return None
        m = (l + r) // 2
        root = TreeNode(nums[m])
        root.left = build(l, m - 1)
        root.right = build(m + 1, r)
        return root
```

- Interview: explain why middle choice keeps the tree balanced.
- Mistakes: always picking one end and creating a skewed tree.
- Product: building a balanced search index from sorted records.
- Practice: sorted array to BST -> preorder to BST variants.

## Trie Fundamentals And Implementation

- For: prefix matching, autocomplete, wildcard-like search structure.
- Signals: strings with shared prefixes.
- Need first: N-ary tree traversal and hash table basics.
- Model: a trie is an N-ary tree where each edge is a character step.
- Steps: walk one character at a time, create child if missing, mark word endings.
- Python:

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
```

- Interview: say tries trade extra space for fast prefix operations.
- Mistakes: forgetting word-end markers, mixing prefix with full-word existence.
- Product: search autocomplete suggestions.
- Practice: insert/search -> startsWith -> wildcard search.
