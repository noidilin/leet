# Advanced Topics

This file collects course-aligned topics that matter but do not need their own standalone file yet.

## LRU Cache

- For: recent-item cache with `O(1)` get and put.
- Signals: design question needing fast lookup plus recent-order updates.
- Need first: hash table enhancements and doubly linked list ideas.
- Model: hash table locates nodes fast, doubly linked list maintains recency order.
- Steps: on access, move node to front; on overflow, evict from tail.
- Python:

```python
# combine key -> node lookup with a doubly linked list
```

- Interview: say LRU is a classic example of combining structures for a stronger design.
- Mistakes: updating the hash table but not the linked list order.
- Product: browser or API response cache.
- Practice: explain design -> implement core methods.

## LFU Cache

- For: optional advanced cache ordered by usage frequency.
- Signals: least-frequently-used eviction rule.
- Need first: LRU cache and hash table enhancements.
- Model: frequency buckets plus recency inside each bucket.
- Steps: update count on every access, move node between frequency lists, evict from the minimum-frequency bucket.
- Python:

```python
# optional advanced topic; usually multiple hash maps plus linked lists
```

- Interview: explain why LFU is harder than LRU.
- Mistakes: not handling ties by recency.
- Product: keeping the most consistently useful items in cache.
- Practice: study after LRU is comfortable.

## Calculator Design

- For: parse and evaluate arithmetic expressions.
- Signals: string expression with operators and parentheses.
- Need first: stack problems and recursion.
- Model: use stacks or recursion to respect precedence and nested expressions.
- Steps: scan tokens, resolve numbers and operators with the right precedence.
- Python:

```python
# stack-based expression evaluation skeleton
```

- Interview: say this is mostly a careful parsing and stack-management problem.
- Mistakes: ignoring whitespace, unary minus, or precedence rules.
- Product: formula evaluation in a spreadsheet-like tool.
- Practice: basic calculator -> parentheses -> multiplication/division.

## Other Classic Design Exercises

- For: classic design questions that combine a few known structures into one tool.
- Signals: design an API, maintain invariants, support multiple operations efficiently.
- Need first: hash table enhancements, stacks, queues, heaps, and linked lists.
- Model: most design exercises are about choosing the right building blocks, then keeping them in sync.
- Steps: list required operations, choose structures for each operation, define invariants, then trace updates carefully.
- Python:

```python
class MyStructure:
    def __init__(self):
        self.data = {}

    def get(self, key):
        pass

    def put(self, key, value):
        pass
```

- Interview: lead with the operation goals and target complexities before code.
- Mistakes: starting to code before deciding the invariant each structure must maintain.
- Product: building a rate limiter, leaderboard helper, or custom history tracker.
- Practice: LRU review -> calculator -> min stack / custom queue / leaderboard-style designs.

## Greedy

- For: choose the locally best action when that can still lead to a global optimum.
- Signals: interval scheduling, jump decisions, coverage, sorting-based local choices.
- Need first: brute-force thinking and proof habit.
- Model: greedy does not start from a memorized template; it starts from a proof idea.
- Steps: propose a local rule, test it against counterexamples, then justify why it is safe.
- Python:

```python
intervals.sort(key=lambda x: x[1])
count = 0
end = float('-inf')
for start, finish in intervals:
    if start >= end:
        count += 1
        end = finish
```

- Interview: always explain why the greedy choice is safe.
- Mistakes: assuming every optimization problem has a greedy solution.
- Product: schedule the most meetings without overlap.
- Practice: interval scheduling -> jump game -> gas station style questions.

## Divide And Conquer

- For: split a problem into smaller independent parts and combine results.
- Signals: recursive split around a midpoint or partition.
- Need first: decomposition-style recursion.
- Model: solve smaller parts separately, then combine.
- Steps: split -> solve left/right -> merge results.
- Python:

```python
def solve(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left = solve(nums[:mid])
    right = solve(nums[mid:])
    return merge(left, right)
```

- Interview: contrast it with traversal-style recursion.
- Mistakes: splitting without gaining efficiency or clarity.
- Product: aggregate analytics in parallel chunks.
- Practice: merge sort -> linked list divide-and-conquer variants.

## Prime Number Techniques

- For: primality and counting primes efficiently.
- Signals: many prime checks or prime-count questions.
- Need first: loops and math basics.
- Model: use divisibility limits or sieve precomputation.
- Steps: for one number, test up to `sqrt(n)`; for many numbers, build a sieve.
- Python:

```python
def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True
```

- Interview: mention why checking past `sqrt(n)` is unnecessary.
- Mistakes: treating 1 as prime.
- Product: simple ID validation rules using prime properties.
- Practice: primality -> sieve -> prime counting.

## Randomized Algorithms

- For: random sampling, shuffling, probabilistic picks.
- Signals: unbiased random selection or randomized balancing.
- Need first: arrays and probability basics.
- Model: randomness can simplify design or give fair sampling.
- Steps: define target distribution first, then implement a method that preserves it.
- Python:

```python
import random
random.shuffle(nums)
```

- Interview: explain why the distribution is uniform or intentionally weighted.
- Mistakes: using biased random formulas.
- Product: game loot tables or randomized experiments.
- Practice: shuffle -> reservoir sampling -> weighted pick.

## Math Tricks

- For: problems that collapse once you notice a number property.
- Signals: repeated parity, gcd, modulo, bit, or symmetry patterns.
- Need first: arithmetic comfort and pattern observation.
- Model: sometimes algebra removes the need for heavy search.
- Steps: try a few examples, look for invariants, then prove the shortcut.
- Python:

```python
# many math tricks are short after the invariant is found
```

- Interview: explain the invariant clearly.
- Mistakes: applying a trick without proving it fits the problem.
- Product: batching IDs by parity or remainder classes.
- Practice: easy parity tricks -> gcd/modulo tricks.

## Scanline

- For: interval overlap and event-sweep problems.
- Signals: meeting rooms, start/end events, active count over time.
- Need first: sorting and prefix-like accumulation.
- Model: turn interval boundaries into sorted events and sweep from left to right.
- Steps: create events, sort them, update active state while sweeping.
- Python:

```python
events = []
for start, end in intervals:
    events.append((start, 1))
    events.append((end, -1))
events.sort()
```

- Interview: say scanline is often a cleaner way to think about overlaps.
- Mistakes: not defining tie-breaking rules for same-time events.
- Product: room booking overlap counts.
- Practice: meeting rooms -> car pooling variants.

## Trapping Rain Water

- For: classic shape-accumulation problem.
- Signals: bars, boundaries, trapped amount between walls.
- Need first: array two pointers or monotonic stack.
- Model: water above a bar depends on the smaller of the best left and right walls.
- Steps: choose prefix-max, two-pointer, or stack framing.
- Python:

```python
left, right = 0, len(height) - 1
left_max = right_max = 0
```

- Interview: explain why the shorter side determines the water level.
- Mistakes: trying to decide water from only one side.
- Product: capacity between usage peaks in a chart.
- Practice: prefix-max version -> two-pointer version.

## Ugly Number Family

- For: generated-number sequences with restricted prime factors.
- Signals: kth ugly number and merged ordered sequences.
- Need first: pointer or heap basics.
- Model: build numbers in increasing order from smaller generated numbers.
- Steps: use multiple pointers or a heap to generate next candidates.
- Python:

```python
ugly = [1]
i2 = i3 = i5 = 0
```

- Interview: say the key is avoiding duplicates while generating in order.
- Mistakes: brute-forcing every integer and testing factors.
- Product: generating allowed version numbers from restricted multipliers.
- Practice: ugly number check -> nth ugly number.

## Weighted Random Pick

- For: pick an index proportionally to its weight.
- Signals: random choice with unequal probabilities.
- Need first: prefix sum and binary search.
- Model: weights create ranges on a number line; sample one point and locate its range.
- Steps: build prefix sums, generate random target, binary search the first prefix that reaches it.
- Python:

```python
import bisect
import random

target = random.randint(1, prefix[-1])
idx = bisect.bisect_left(prefix, target)
```

- Interview: connect weighted pick to prefix sum plus binary search.
- Mistakes: using `random.choice` directly on weights.
- Product: show items with probability proportional to score.
- Practice: prefix sum review -> weighted pick.

## nSum Framework

- For: 2Sum, 3Sum, 4Sum, and generalized sum problems.
- Signals: find tuples that reach a target.
- Need first: sorting and array two pointers.
- Model: reduce `nSum` to `(n - 1)Sum` until the 2Sum base case.
- Steps: sort, fix one value, recurse on the smaller problem, use two pointers at the base.
- Python:

```python
def two_sum(nums, start, target):
    left, right = start, len(nums) - 1
```

- Interview: explain the recursive reduction and duplicate-skipping rules.
- Mistakes: not sorting first or not skipping duplicates.
- Product: choose bundles of items to hit a target budget.
- Practice: 2Sum -> 3Sum -> 4Sum.

## Sorting Overview

- For: interview discussion of classic sorting ideas and tradeoffs.
- Signals: asked about complexity, stability, or use cases.
- Need first: arrays and divide-and-conquer basics.
- Model: different sorts trade simplicity, worst-case guarantees, memory use, and stability.
- Steps: know when to mention quick sort, merge sort, heap sort, counting-based sorts, and built-in sort behavior.
- Python:

```python
nums.sort()
```

- Interview: focus on time complexity, space, stability, and when a built-in sort is enough.
- Mistakes: trying to memorize all implementation details before understanding tradeoffs.
- Product: sorting feed items by score or timestamp.
- Practice: compare major sorts conceptually before implementing any one of them.
