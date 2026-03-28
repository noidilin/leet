# Dynamic Programming

Dynamic programming is optimized brute force for problems with overlapping subproblems.

## DP Framework

- For: optimization and counting problems with repeated subproblems.
- Signals: brute-force recursion repeats the same state many times.
- Need first: recursion, tree thinking, memoization basics.
- Model: start from brute force, then cache repeated states, then rewrite iteratively when useful.
- Steps: define state -> write transition -> choose base case -> add memo -> consider bottom-up order.
- Python:

```python
from functools import lru_cache

@lru_cache(None)
def dp(state):
    if base_case(state):
        return base_value
    return best_of(transitions_from(state))
```

- Interview: always connect brute force, overlap, memoization, and optional iterative rewrite.
- Mistakes: trying to memorize tables without first defining the state clearly.
- Product: planning the best result across repeated decision states.
- Practice: memoized recursion -> tabulation -> space optimization.

## State Definition

- For: deciding what one DP entry means.
- Signals: confusion about what `dp[i]` or `dp[i][j]` should store.
- Need first: DP framework.
- Model: state should capture exactly enough information to continue the problem.
- Steps: say the meaning in a full sentence before coding.
- Python:

```python
# example: dp[i] = best answer for nums[:i + 1]
```

- Interview: define state in words before writing formulas.
- Mistakes: choosing a state that is too weak or too large.
- Product: best profit up to day `i`.
- Practice: 1D state -> 2D state -> state compression.

## Transition Derivation

- For: writing the recurrence from smaller states.
- Signals: you know the state but not how states connect.
- Need first: state definition.
- Model: ask what last choice or last action leads into this state.
- Steps: split by the last move, take max/min/sum as required.
- Python:

```python
# example: dp[i] = max(dp[i - 1], take_current_option)
```

- Interview: derive transition from problem meaning, not memory.
- Mistakes: copying a formula without explaining the last-step logic.
- Product: extending a best schedule by one more day.
- Practice: Fibonacci-style -> LIS-style -> edit distance.

## Base Case And Memo Initialization

- For: starting the recurrence safely.
- Signals: index errors, empty input confusion, impossible states.
- Need first: state and transition.
- Model: the base case is the smallest state whose answer is already known.
- Steps: write empty/smallest cases first, then initialize memo or table accordingly.
- Python:

```python
dp = [0] * (n + 1)
dp[0] = 0
```

- Interview: explain why the base case matches the state meaning.
- Mistakes: using a base case that does not fit the recurrence.
- Product: zero days of work gives zero profit.
- Practice: simple 1D DP -> 2D table initialization.

## Traversal Order

- For: filling bottom-up DP tables correctly.
- Signals: state depends on previous row, next row, left cell, or diagonal.
- Need first: transition and base cases.
- Model: fill states only after the states they depend on are already known.
- Steps: inspect dependencies, then choose row order, column order, or reverse order.
- Python:

```python
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = ...
```

- Interview: justify order from the recurrence.
- Mistakes: filling left-to-right when the formula depends on future cells.
- Product: building cumulative edit results one prefix at a time.
- Practice: 1D forward -> 1D backward -> 2D grid DP.

## LIS

- For: classic DP design prototype.
- Signals: longest increasing subsequence or subsequence ordering questions.
- Need first: DP framework.
- Model: `dp[i]` often means the best subsequence ending at `i`.
- Steps: try all previous `j < i`, extend when `nums[j] < nums[i]`.
- Python:

```python
dp = [1] * len(nums)
for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
```

- Interview: explain ending-at-i state first, then mention `O(n log n)` as a later optimization.
- Mistakes: mixing subsequence with subarray.
- Product: longest improving trend in engagement metrics.
- Practice: LIS `O(n^2)` -> count variants -> optimized version.

## Edit Distance

- For: string transformation with insert/delete/replace choices.
- Signals: minimum operations to convert one string to another.
- Need first: 2D DP, state and transition.
- Model: `dp[i][j]` is the best answer for prefixes of length `i` and `j`.
- Steps: compare last characters; if equal, inherit diagonal, else take best of three operations.
- Python:

```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = i
for j in range(n + 1):
    dp[0][j] = j
```

- Interview: explain what the three operations mean in the table.
- Mistakes: forgetting the meaning of `i` and `j` as prefix lengths.
- Product: measuring how different two typed queries are.
- Practice: delete distance -> full edit distance.

## Maximum Subarray

- For: best contiguous segment.
- Signals: maximum sum over a continuous range.
- Need first: 1D DP thinking.
- Model: `dp[i]` is the best subarray ending at `i`.
- Steps: either extend previous subarray or start fresh at current element.
- Python:

```python
best = cur = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)
    best = max(best, cur)
```

- Interview: say this is DP even though the final code is very short.
- Mistakes: confusing it with subsequence problems.
- Product: best streak of daily gain.
- Practice: Kadane -> circular variants.

## LCS

- For: longest common subsequence between two sequences.
- Signals: match while allowing skips.
- Need first: 2D DP and prefix-state thinking.
- Model: if last items match, take diagonal plus one; otherwise drop one side and take the best.
- Steps: define `dp[i][j]` on prefixes, then fill table.
- Python:

```python
if a[i - 1] == b[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
else:
    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
```

- Interview: contrast subsequence with substring.
- Mistakes: requiring continuity when the problem allows skips.
- Product: compare two edit histories for shared structure.
- Practice: LCS -> uncrossed lines -> diff-style variants.

## 0/1 Knapsack

- For: choose items once each under capacity limit.
- Signals: weight/capacity plus maximize value.
- Need first: DP state and transition.
- Model: for each item, either take it or skip it.
- Steps: `dp[i][w]` or compressed `dp[w]`, then update from high to low capacity.
- Python:

```python
dp = [0] * (capacity + 1)
for weight, value in items:
    for w in range(capacity, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)
```

- Interview: explain why reverse order prevents reusing the same item twice.
- Mistakes: iterating forward and accidentally turning it into complete knapsack.
- Product: fit the best feature set into limited engineering time.
- Practice: classic knapsack -> partition/subset variants.

## Subset Knapsack

- For: subset-sum style yes/no or counting questions.
- Signals: can we reach exact target with each item used at most once?
- Need first: 0/1 knapsack.
- Model: same take-or-skip choice, but the goal is feasibility or count instead of value.
- Steps: define boolean or count DP over capacity/target.
- Python:

```python
dp = [False] * (target + 1)
dp[0] = True
for x in nums:
    for s in range(target, x - 1, -1):
        dp[s] = dp[s] or dp[s - x]
```

- Interview: say this is the same skeleton as 0/1 knapsack with different DP meaning.
- Mistakes: not redefining what `dp[s]` means.
- Product: can a set of tasks exactly fill available time?
- Practice: subset sum -> partition equal subset sum.

## Complete Knapsack

- For: choose an item unlimited times.
- Signals: coin change or unbounded reuse.
- Need first: 0/1 knapsack.
- Model: same item can be taken again, so update order changes.
- Steps: iterate capacity forward so current item can contribute multiple times.
- Python:

```python
dp = [0] * (amount + 1)
for coin in coins:
    for s in range(coin, amount + 1):
        dp[s] = max(dp[s], dp[s - coin] + value_of(coin))
```

- Interview: emphasize that forward traversal is the key difference from 0/1 knapsack.
- Mistakes: using reverse order and blocking reuse.
- Product: unlimited coupon denominations in a payment system.
- Practice: coin change -> complete knapsack variants.
