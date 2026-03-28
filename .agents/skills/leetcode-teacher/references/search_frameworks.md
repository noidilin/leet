# Search Frameworks

These frameworks cover brute-force search, structured enumeration, and shortest-path search in unweighted state spaces.

## Backtracking Framework

- For: enumerate all valid choices or build one valid arrangement by trying and undoing.
- Signals: permutations, combinations, path construction, constraint satisfaction.
- Need first: recursion from binary tree perspective.
- Model: each recursive level chooses one branch in a decision tree.
- Steps: choose -> recurse -> undo choice.
- Python:

```python
result = []

def backtrack(path):
    if is_solution(path):
        result.append(path[:])
        return
    for choice in choices:
        if not valid(choice, path):
            continue
        path.append(choice)
        backtrack(path)
        path.pop()
```

- Interview: say backtracking is organized brute force with pruning.
- Mistakes: forgetting the undo step.
- Product: generate valid team combinations.
- Practice: subset generation -> combinations -> constrained search.

## Permutation / Combination / Subset Framework

- For: the three most common backtracking families.
- Signals: choose all orderings, choose fixed-size groups, choose any subset.
- Need first: backtracking framework.
- Model: the main difference is whether order matters and whether you can reuse positions.
- Steps: define the decision tree, start index, and used-state rules.
- Python:

```python
def subsets(nums):
    ans = []
    path = []
    def dfs(start):
        ans.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
```

- Interview: explain how start index avoids duplicates for subset/combination style problems.
- Mistakes: mixing permutation rules with combination rules.
- Product: choosing feature bundles or seating groups.
- Practice: subsets -> combinations -> permutations.

## Constraint Backtracking: Sudoku And N-Queens

- For: search with strong validity rules.
- Signals: place items under row/column/box/diagonal constraints.
- Need first: backtracking and set-based pruning.
- Model: prune early whenever a partial choice already breaks a rule.
- Steps: choose next position, test constraint, recurse, undo.
- Python:

```python
# keep row/col/box or diagonal sets for fast validity checks
```

- Interview: say the key optimization is pruning invalid branches as early as possible.
- Mistakes: rechecking the whole board every time instead of maintaining sets.
- Product: assigning resources without conflicts.
- Practice: N-Queens -> Sudoku.

## Island / Flood-Fill DFS Framework

- For: connected-region problems on grids.
- Signals: islands, rooms, components, flood fill.
- Need first: DFS, 2D traversal.
- Model: each unvisited land cell starts a DFS over one connected component.
- Steps: loop cells, start DFS on a new component, mark visited as soon as you enter.
- Python:

```python
def dfs(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '0'
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
```

- Interview: say this is graph DFS on an implicit graph.
- Mistakes: marking visited too late and revisiting the same cell.
- Product: flood fill in an image editor.
- Practice: count islands -> max area -> perimeter variants.

## DFS Vs Backtracking

- For: distinguishing traversal from choice enumeration.
- Signals: either explore a structure or search a decision tree.
- Need first: DFS and backtracking basics.
- Model: DFS explores existing edges; backtracking creates choices and undoes them.
- Steps: ask whether neighbors already exist in the input or are choices you are building.
- Python:

```python
# DFS: follow existing neighbors
# Backtracking: try candidate choices and undo
```

- Interview: say many backtracking solutions are written with DFS syntax, but the mental model is different.
- Mistakes: using the terms interchangeably without clarifying the state meaning.
- Product: DFS for exploring a file graph, backtracking for generating candidate passwords.
- Practice: compare island DFS with subsets backtracking.

## BFS Framework

- For: shortest number of steps in an unweighted state space.
- Signals: minimum moves, nearest target, level-by-level expansion.
- Need first: queue and level-order traversal.
- Model: BFS explores all states at distance `d` before any state at distance `d + 1`.
- Steps: enqueue start state, mark visited early, expand by layers.
- Python:

```python
from collections import deque

def bfs(start):
    q = deque([(start, 0)])
    visited = {start}
    while q:
        state, dist = q.popleft()
```

- Interview: connect BFS to level-order traversal on trees.
- Mistakes: marking visited after dequeue instead of when enqueuing.
- Product: minimum clicks to reach a page.
- Practice: simple graph shortest path -> state-space puzzles.

## BFS Shortest-Path Framework

- For: explicit shortest path problems on unweighted graphs or grids.
- Signals: maze, mutation steps, word ladder, nearest exit.
- Need first: BFS framework.
- Model: the first time BFS reaches a state is the shortest path to that state.
- Steps: define state, transitions, visited rule, and termination condition.
- Python:

```python
def shortest_path(start, target):
    q = deque([(start, 0)])
    visited = {start}
    while q:
        state, dist = q.popleft()
        if state == target:
            return dist
```

- Interview: explain why uniform edge cost makes layer order equal to shortest distance.
- Mistakes: using DFS and hoping to find the shortest path first.
- Product: minimum hops between users or shortest maze exit.
- Practice: grid shortest path -> word ladder style state search.
