# Stack And Queue Frameworks

These topics come after stack and queue fundamentals and focus on problem-solving frameworks.

## Stack Via Queue / Queue Via Stack

- For: understanding how behavior can be built from restricted operations.
- Signals: design question about simulating one structure with another.
- Need first: queue fundamentals and stack fundamentals.
- Model: the hidden cost moves into rearranging operations.
- Steps: decide whether push or pop should be expensive, then preserve the target behavior.
- Python:

```python
from collections import deque

q = deque()
```

- Interview: explain which operation becomes costly and why the behavior is still correct.
- Mistakes: only copying values without preserving order semantics.
- Product: building one API on top of another restricted API.
- Practice: stack via queues -> queue via stacks.

## Classic Stack Problems

- For: nested structure, previous greater/smaller ideas, expression parsing, undo-style flow.
- Signals: matching brackets, remove adjacent pairs, next item depends on recent history.
- Need first: stack fundamentals.
- Model: the top of the stack stores unfinished work.
- Steps: push when opening work, pop when closing or resolving work.
- Python:

```python
stack = []
pairs = {'(': ')', '[': ']', '{': '}'}
for ch in s:
    if ch in pairs:
        stack.append(ch)
    elif not stack or pairs[stack.pop()] != ch:
        return False
return not stack
```

- Interview: say stacks are ideal when the newest unresolved item matters most.
- Mistakes: not checking empty stack before pop.
- Product: undo and nested command parsing in an editor.
- Practice: valid parentheses -> decode string -> expression evaluation.

## Classic Queue Problems

- For: first-in-first-out workflows, layered processing, scheduling.
- Signals: tasks arrive in order, breadth-first expansion.
- Need first: queue fundamentals.
- Model: the queue stores the frontier of work.
- Steps: push new work at the back, process old work from the front.
- Python:

```python
from collections import deque

queue = deque([start])
while queue:
    cur = queue.popleft()
```

- Interview: connect queue behavior to BFS and real scheduling systems.
- Mistakes: forgetting level boundaries when the problem asks for layers.
- Product: customer support tickets processed by arrival order.
- Practice: simple queue simulation -> level order traversal -> multi-source BFS preview.

## Monotonic Stack

- For: next greater/smaller element and range influence questions.
- Signals: for each position, ask about the first larger or smaller value on one side.
- Need first: stack problems and array traversal.
- Model: keep the stack ordered so useless candidates are removed immediately.
- Steps: while the top breaks monotonic order, pop; then use the remaining top as the answer context.
- Python:

```python
stack = []
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        answer[j] = x
    stack.append(i)
```

- Interview: explain what the stack stores and why popped items will never matter again.
- Mistakes: storing values when indexes are needed.
- Product: for each day, find the next day with a higher metric.
- Practice: next greater element -> daily temperatures -> largest rectangle.

## Monotonic Queue

- For: sliding window maximum or minimum.
- Signals: window moves one step at a time and needs best value quickly.
- Need first: queue behavior, sliding window.
- Model: keep a deque of useful candidates in monotonic order.
- Steps: remove expired indexes from the front, remove weaker candidates from the back, then read the best from the front.
- Python:

```python
from collections import deque

window = deque()
for i, x in enumerate(nums):
    while window and window[0] <= i - k:
        window.popleft()
    while window and nums[window[-1]] <= x:
        window.pop()
    window.append(i)
```

- Interview: compare it with a heap and note that monotonic queue gives true `O(n)` traversal.
- Mistakes: forgetting to evict expired indexes.
- Product: keep the hottest topic in the latest time window.
- Practice: sliding window max -> min max variants.
