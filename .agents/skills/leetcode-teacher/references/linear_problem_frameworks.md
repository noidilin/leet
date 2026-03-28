# Linear Problem Frameworks

Use these frameworks for linked lists, arrays, strings, and grid-like linear traversals.

## Linked List Two Pointers

- For: cycle detection, middle node, kth-from-end, merge-style pointer movement.
- Signals: one-pass linked list question with two moving references.
- Need first: linked list fundamentals.
- Model: move pointers at different speeds or with different starting offsets.
- Steps: define what each pointer means, move carefully, stop on `None` checks.
- Python:

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

- Interview: explain pointer meaning before code.
- Mistakes: forgetting `fast.next`, moving in wrong order.
- Product: detect circular dependency in a chain of package references.
- Practice: middle node -> cycle detection -> kth from end.

## Linked List Reversal

- For: reverse all or part of a linked list.
- Signals: pointer direction must flip.
- Need first: linked lists and temporary variables.
- Model: cut current node away, point it backward, then advance.
- Steps: store `next`, reverse `curr.next`, move `prev` and `curr`.
- Python:

```python
prev = None
curr = head
while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
```

- Interview: say the key is preserving `next_node` before rewiring.
- Mistakes: losing the rest of the list.
- Product: reversing playback history order for export.
- Practice: full reverse -> reverse first k -> reverse a sublist.

## Linked List Palindrome

- For: compare front half and back half of a list.
- Signals: same forward and backward, but list has no random access.
- Need first: linked list two pointers and reversal.
- Model: find the middle, reverse one half, compare node by node.
- Steps: middle -> reverse second half -> compare -> optionally restore.
- Python:

```python
def is_palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
```

- Interview: mention `O(n)` time and `O(1)` extra space with in-place reversal.
- Mistakes: mishandling odd-length lists.
- Product: checking whether a user action sequence mirrors itself.
- Practice: array palindrome -> linked list palindrome with extra array -> in-place version.

## Array Two Pointers

- For: pair search, deduplication, compaction, partitioning.
- Signals: array or string with two moving boundaries.
- Need first: arrays and indexing.
- Model: each pointer marks a region or candidate.
- Steps: define left meaning and right meaning before coding.
- Python:

```python
left, right = 0, len(nums) - 1
while left < right:
    total = nums[left] + nums[right]
    if total == target:
        return [left, right]
    if total < target:
        left += 1
    else:
        right -= 1
```

- Interview: explain why sorted order makes pointer movement valid.
- Mistakes: using this on unsorted data without justification.
- Product: find two IDs whose combined cost hits a budget.
- Practice: pair sum -> remove duplicates -> partition colors.

## 2D Array Traversal

- For: matrix scans, diagonals, spiral order, layer-based movement.
- Signals: row and column rules matter.
- Need first: arrays and loops.
- Model: a 2D array is still an array; you just need a clear visiting order.
- Steps: decide coordinate system, boundary rules, and update order.
- Python:

```python
for r in range(rows):
    for c in range(cols):
        visit(grid[r][c])
```

- Interview: say the hard part is boundary control, not the nested loop itself.
- Mistakes: row/column confusion and boundary off-by-one bugs.
- Product: scanning seats in a theater grid.
- Practice: row-major -> column-major -> diagonal -> spiral.

## Sliding Window

- For: contiguous subarray or substring questions.
- Signals: "longest", "shortest", or "count" inside a moving range.
- Need first: arrays, hash tables, two pointers.
- Model: maintain a valid window and grow or shrink it.
- Steps: expand right, update state, shrink left while rule is broken or can be improved.
- Python:

```python
left = 0
for right in range(len(nums)):
    add(nums[right])
    while window_is_invalid():
        remove(nums[left])
        left += 1
```

- Interview: state what makes the window valid and when it shrinks.
- Mistakes: not defining the window invariant.
- Product: trending topics in the last k posts or minutes.
- Practice: fixed-size sum -> variable-size longest substring -> minimum window.

## Binary Search

- For: ordered search space with yes/no direction decisions.
- Signals: sorted array, monotonic condition, first/last true boundary.
- Need first: arrays and loop invariants.
- Model: each comparison removes half the search space.
- Steps: choose interval style, keep invariant consistent, move toward the answer.
- Python:

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

- Interview: define the invariant and why each branch is safe.
- Mistakes: mixing closed and half-open interval rules.
- Product: find the first bad version in a deployment timeline.
- Practice: exact match -> left boundary -> right boundary.

## Binary Search Application Thinking

- For: problems where the answer is not stored directly but the condition is monotonic.
- Signals: "minimum feasible", "maximum possible", "first time", "smallest capacity".
- Need first: binary search and monotonic reasoning.
- Model: binary search the answer, not the data.
- Steps: define answer range, write a feasibility check, then search for the first valid answer.
- Python:

```python
def first_true(lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

- Interview: say the real work is proving `feasible(x)` is monotonic.
- Mistakes: writing a check that changes meaning across cases.
- Product: smallest server capacity that can handle all requests.
- Practice: first bad version -> capacity problems -> rate/time feasibility.

## Prefix Sum

- For: repeated range-sum queries or converting many additions into one lookup.
- Signals: many subarray sum queries, quick cumulative totals.
- Need first: arrays.
- Model: store total up to each position so range sum becomes subtraction.
- Steps: build prefix once, answer each query as `pre[r + 1] - pre[l]`.
- Python:

```python
pre = [0]
for x in nums:
    pre.append(pre[-1] + x)

range_sum = pre[right + 1] - pre[left]
```

- Interview: explain the extra leading zero and why it simplifies boundaries.
- Mistakes: off-by-one indexing.
- Product: cumulative engagement queries over daily traffic.
- Practice: range sum -> subarray count variants -> 2D prefix sum preview.

## Difference Array

- For: many range updates before a final reconstruction.
- Signals: add value to every element in many intervals.
- Need first: prefix sum idea.
- Model: mark where change starts and where it stops, then recover final values with a running sum.
- Steps: update boundaries in `diff`, then prefix-sum the `diff` array.
- Python:

```python
diff[left] += val
if right + 1 < len(diff):
    diff[right + 1] -= val
```

- Interview: contrast prefix sum for fast queries with difference array for fast updates.
- Mistakes: forgetting to rebuild the final array.
- Product: batch booking updates across seat ranges.
- Practice: single interval updates -> many updates -> flight booking style problems.
